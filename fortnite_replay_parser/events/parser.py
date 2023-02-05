from events.match import read_match_stats_buffer, read_team_stats_buffer
from events.player import read_elimination_buffer
from models.fortnite import EventTypes
from models.events import *
from logger import logger


class EventParser:
    def __init__(self, reader):
        self.reader = reader

    def parse(self):
        event_id = self.reader.replay.read_string()
        group = self.reader.replay.read_string()
        metadata = self.reader.replay.read_string()
        start_time = self.reader.replay.read_uint32()
        end_time = self.reader.replay.read_uint32()
        size = self.reader.replay.read_uint32()

        event_buffer = self.reader.decrypt_buffer(size)

        logger.debug(
            "parsing event: " + event_id + " " + group + " " + metadata
        )

        event = None
        # player events
        if group == EventTypes.PLAYER_ELIMINATION.value:
            event = PlayerEliminationEvent(
                event_id, group, metadata, start_time, end_time
            )
            read_elimination_buffer(event, self.reader.header, event_buffer)

        # match events
        if metadata == EventTypes.MATCH_STATS.value:
            event = MatchStatsEvent(
                event_id, group, metadata, start_time, end_time
            )
            read_match_stats_buffer(event, event_buffer)
        elif metadata == EventTypes.TEAM_STATS.value:
            event = TeamStatsEvent(
                event_id, group, metadata, start_time, end_time
            )
            read_team_stats_buffer(event, event_buffer)

        return event
