from datetime import datetime
from typing import Union
from pydantic.dataclasses import dataclass

@dataclass
class Event:
    event_id: str
    group: str
    metadata: str
    start_time: int
    end_time: int


@dataclass
class PlayerEliminationEvent(Event):
    eliminated: str = None
    eliminator: str = None
    gun_type: Union[str, int] = None
    knocked: bool = None


@dataclass
class MatchStatsEvent(Event):
    accuracy: int = None
    assists: int = None
    eliminations: int = None
    weaponDamage: int = None
    otherDamage: int = None
    revives: int = None
    damageTaken: int = None
    damageToStructures: int = None
    materialsGathered: int = None
    materialsUsed: int = None
    totalTraveled: int = None
    damageToPlayers: int = None


@dataclass
class TeamStatsEvent(MatchStatsEvent):
    placement: int = None
    totalPlayers: int = None
