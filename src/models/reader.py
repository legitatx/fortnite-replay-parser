from enum import Enum
from typing import List, Tuple

from pydantic import BaseModel

class BitTypes(Enum):
    """See bitstring for more types"""

    INT_32 = "intle:32"
    UINT8 = "uint:8"
    UINT_16 = "uintle:16"
    UINT_32 = "uintle:32"
    UINT_64 = "uintle:64"
    FLOAT_LE_32 = "floatle:32"
    BIT = "bin:1"
    BYTE = "bytes:1"
    BOOL = "bool"


class ChunkTypes(Enum):
    """Replay chunk types as defined by Unreal Engine"""

    HEADER = 0
    REPLAY_DATA = 1
    CHECKPOINT = 2
    EVENT = 3


class Header(BaseModel):
    magic: int
    network_version: int
    network_checksum: int
    engine_network_version: int
    game_network_protocol: int
    guid: str
    major: int
    minor: int
    patch: int
    changelist: int
    branch: str
    levelnames_and_times: List[Tuple[str, int]]
    flags: int
    game_specific_data: List[str]


class Metadata(BaseModel):
    file_version: int
    length_in_ms: int
    network_version: int
    changelist: int
    friendly_name: str
    is_live: bool
    timestamp: int
    is_compressed: bool
    is_encrypted: bool
    encryption_key: bytes
