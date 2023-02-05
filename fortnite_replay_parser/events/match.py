from models.events import MatchStatsEvent, TeamStatsEvent


def read_match_stats_buffer(event: MatchStatsEvent, buffer):
    buffer.skip_bytes(4)
    event.accuracy = int(buffer.read_float32())
    event.assists = buffer.read_uint32()
    event.eliminations = buffer.read_uint32()
    event.weapon_damage = buffer.read_uint32()
    event.other_damage = buffer.read_uint32()
    event.revives = buffer.read_uint32()
    event.damage_taken = buffer.read_uint32()
    event.damage_to_structures = buffer.read_uint32()
    event.materials_gathered = buffer.read_uint32()
    event.materials_used = buffer.read_uint32()
    event.total_traveled = round(buffer.read_uint32() / 100000.0)
    event.damage_to_players = event.other_damage + event.weapon_damage


def read_team_stats_buffer(event: TeamStatsEvent, buffer):
    buffer.skip_bytes(4)
    event.placement = buffer.read_uint32()
    event.totalPlayers = buffer.read_uint32()
