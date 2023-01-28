from typing import Dict, List, Optional, Union
from pydantic import BaseModel


class FVector(BaseModel):
    x: float
    y: float
    z: float


class Vector4D(BaseModel):
    x: float
    y: float
    z: float
    w: float


class FRotate(BaseModel):
    pitch: float
    yaw: float
    roll: float


class PlayerElimination(BaseModel):
    name: str
    rotation: Optional[Vector4D]
    location: Optional[FVector]
    scale: Optional[FVector]


class SafeZone(BaseModel):
    x: float
    y: float
    z: float
    radius: float


class DeathInfo(BaseModel):
    id: str
    reason: str
    time: int


class PlayerPosition(BaseModel):
    x: float
    y: float
    z: float
    movementType: Optional[str]


class PlayerKill(BaseModel):
    playerId: str
    reason: str
    knocked: bool
    location: FVector
    time: int


class Player(BaseModel):
    id: str
    positions: Dict[int, PlayerPosition]  # timestamp -> position
    killScore: int
    kills: List[PlayerKill]
    knockInfo: Optional[DeathInfo]
    elimInfo: Optional[DeathInfo]
