from datetime import datetime
from typing import Dict, List, Optional, Union
from pydantic import BaseModel

from src.models.fortnite import FVector, Player, SafeZone


class PlayerEliminationEvent(BaseModel):
    eliminated: str
    eliminator: str
    gun_type: Union[str, int]
    knocked: bool


class MatchStatsEventExport(BaseModel):
    accuracy: int
    assists: int
    eliminations: int
    weaponDamage: int
    otherDamage: int
    revives: int
    damageTaken: int
    damageToStructures: int
    materialsGathered: int
    materialsUsed: int
    totalTraveled: int
    damageToPlayers: int


class TeamStatsEventExport(MatchStatsEventExport):
    placement: int
    totalPlayers: int


class MatchStatsEvent(TeamStatsEventExport):
    pass


class GFPEvent(BaseModel):
    moduleId: str
    moduleVersion: Optional[float]
    artifactId: Optional[str]


class Events:
    chests: List[FVector]
    safeZones: List[SafeZone]
    players: List[Player]
    matchStats: MatchStatsEvent
    gfp: List[GFPEvent]


class GlobalDataEvents:
    chests: List[FVector]
    safeZones: List[SafeZone]
    players: Dict[str, Player]
    matchStats: Optional[MatchStatsEvent]
    gfp: Optional[List[GFPEvent]]
    timecode: Optional[datetime]
