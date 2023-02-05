from exceptions import PlayerEliminationException
from models.events import PlayerEliminationEvent
from models.reader import Header
from models.fortnite import EFortWeaponType


def get_player_name(buffer):
    player_type = buffer.read_byte()
    if player_type == 0x03:
        return "Bot"
    elif player_type == 0x10:
        return buffer.read_string()
    elif player_type == 0x11:
        buffer.skip_bytes(1)
        return buffer.read_guid()
    else:
        raise PlayerEliminationException()


def read_elimination_buffer(
    event: PlayerEliminationEvent, header: Header, buffer
):
    if header.engine_network_version >= 11 and header.major >= 9:
        if header.engine_network_version >= 23:
            buffer.skip_bytes(5 + (80 * 2))
        else:
            buffer.skip_bytes(85)
        event.eliminated = get_player_name(buffer)
        event.eliminator = get_player_name(buffer)
    else:
        if header.major <= 4 and header.minor < 2:
            buffer.skip(12)
        elif header.major == 4 and header.minor <= 2:
            buffer.skip(40)
        else:
            buffer.skip(45)

        event.eliminated = buffer.read_string()
        event.eliminator = buffer.read_string()

    gun_byte = buffer.read_byte()
    try:
        gun = EFortWeaponType(gun_byte)
        event.gun_type = gun.name
    except ValueError:
        event.gun_type = gun_byte
    event.knocked = buffer.read_uint32()
