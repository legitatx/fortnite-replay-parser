from typing import List, Union

from Crypto.Cipher import AES
from events.parser import EventParser

from exceptions import InvalidReplayException
from logger import logger
from models import ChunkTypes, Header
from models.events import Event
from models.reader import Metadata
from utils import ConstBitStreamWrapper, VERSION_REGEX

GAME_METADATA_MAGIC = 0x1CA2E27F
HEADER_MAGIC = 0x2CF5A13D


class FortniteReplayReader:
    """Replay reader class to use as a context manager.

    Can be used with either a file path or a stream of bytes:
    >>> with FortniteReplayReader('filepath') as replay:
            print(replay.stats)
    >>> f = open('filepath', 'rb')
    >>> with FortniteReplayReader(f.read()) as replay:
            print(replay.stats)
    >>> f.close()
    """

    _close_on_exit = False

    def __init__(self, src):
        self.src: Union[str, bytes] = src
        self._file = None
        self.replay: ConstBitStreamWrapper = None
        self.metadata: Metadata = None
        self.header: Header = None
        self.event_parser = EventParser(self)
        self.events: List[Event] = []

    def __len__(self):
        return self.replay.len

    def __sizeof__(self):
        return self.replay.len

    def __enter__(self):
        logger.info(
            f"Context manager entered scope. Parsing replay file: {self.src}"
        )

        if isinstance(self.src, str):
            self._file = open(self.src, "rb")
            self._close_on_exit = True
        elif isinstance(self.src, bytes):
            self._file = self.src
        else:
            raise TypeError()

        self.replay = ConstBitStreamWrapper(self._file)
        self.parse_metadata()
        self.parse_chunks()
        return self

    def __exit__(self, *args):
        logger.info(f"Context manager no longer in scope for file: {self.src}")

        if self._close_on_exit:
            self._file.close()

    def parse_metadata(self):
        logger.info("Parsing replay metadata...")

        magic = self.replay.read_uint32()
        if magic != GAME_METADATA_MAGIC:
            raise InvalidReplayException()
        file_version = self.replay.read_uint32()
        length_in_ms = self.replay.read_uint32()
        network_version = self.replay.read_uint32()
        changelist = self.replay.read_uint32()
        friendly_name = self.replay.read_string().strip()
        is_live = self.replay.read_bool()

        if file_version >= 3:
            timestamp = self.replay.read_uint64()
        if file_version >= 2:
            is_compressed = self.replay.read_bool()

        is_encrypted, encryption_key = False, bytearray()
        if file_version >= 6:
            is_encrypted = self.replay.read_bool()
            encryption_key = self.replay.read_bytes(self.replay.read_uint32())

        if not is_live and is_encrypted and len(encryption_key) == 0:
            raise InvalidReplayException(
                "Completed replay is marked encrypted but has no key!"
            )

        if is_live and is_encrypted:
            raise InvalidReplayException(
                "Replay is marked encrypted but not yet marked as completed!"
            )

        self.metadata = Metadata(
            file_version=file_version,
            length_in_ms=length_in_ms,
            network_version=network_version,
            changelist=changelist,
            friendly_name=friendly_name,
            is_live=is_live,
            timestamp=timestamp,
            is_compressed=is_compressed,
            is_encrypted=is_encrypted,
            encryption_key=encryption_key,
        )

    def parse_chunks(self):
        logger.info("Parsing replay chunks...")

        while self.replay.pos < len(self.replay):
            chunk_type = self.replay.read_uint32()
            chunk_size = self.replay.read_int32()
            offset = self.replay.bytepos

            if chunk_type == ChunkTypes.HEADER.value:
                self.parse_header()
            elif chunk_type == ChunkTypes.EVENT.value:
                self.parse_event()
            elif chunk_type == ChunkTypes.CHECKPOINT.value:
                pass # TODO: Implement
            elif chunk_type == ChunkTypes.REPLAY_DATA.value:
                pass # TODO: Implement

            self.replay.bytepos = offset + chunk_size

    def parse_event(self):
        event = self.event_parser.parse()
        self.events.append(event)

    def parse_header(self) -> None:
        logger.info("Parsing Unreal Engine meta (header) from replay...")

        magic = self.replay.read_uint32()
        if magic != HEADER_MAGIC:
            raise InvalidReplayException()
        network_version = self.replay.read_uint32()
        network_checksum = self.replay.read_uint32()
        engine_network_version = self.replay.read_uint32()
        game_network_protocol = self.replay.read_uint32()

        if network_version >= 12:
            guid = self.replay.read_guid()

        if network_version >= 11:
            self.replay.skip_bytes(4)
            patch = self.replay.read_uint16()
            changelist = self.replay.read_uint32()

            branch = self.replay.read_string()
            match = VERSION_REGEX.search(branch)
            major, minor = match.group(1), match.group(2)
        else:
            changelist = self.replay.read_uint32()

        if network_version >= 18:
            self.replay.skip_bytes(12)

        levelnames_and_times = self.replay.read_tuple_array(
            self.replay.read_string, self.replay.read_uint32
        )

        if network_version >= 9:
            flags = self.replay.read_uint32()

        game_specific_data = self.replay.read_array(self.replay.read_string)

        self.header = Header(
            magic=magic,
            network_version=network_version,
            network_checksum=network_checksum,
            engine_network_version=engine_network_version,
            game_network_protocol=game_network_protocol,
            guid=guid,
            major=major,
            minor=minor,
            patch=patch,
            changelist=changelist,
            branch=branch,
            levelnames_and_times=levelnames_and_times,
            flags=flags,
            game_specific_data=game_specific_data,
        )

    def decrypt_buffer(self, size) -> ConstBitStreamWrapper:
        if not self.metadata.is_encrypted:
            return ConstBitStreamWrapper(self.replay.read_bytes(size))

        key = self.metadata.encryption_key
        encrypted_bytes = self.replay.read_bytes(size)

        aes = AES.new(key, mode=AES.MODE_ECB)
        return ConstBitStreamWrapper(aes.decrypt(encrypted_bytes))
