from enum import Enum


class EventTypes(Enum):
    PLAYER_ELIMINATION = "playerElim"
    MATCH_STATS = "AthenaMatchStats"
    TEAM_STATS = "AthenaMatchTeamStats"
    ENCRYPTION_KEY = "PlayerStateEncryptionKey"
    CHARACTER_SAMPLE = "CharacterSampleMeta"
    ZONE_UPDATE = "ZoneUpdate"
    BATTLE_BUS = "BattleBusFlight"


class BuildTargetType(Enum):
    UNKNOWN = 0
    GAME = 1
    SERVER = 2
    CLIENT = 3
    EDITOR = 4
    PROGRAM = 5


class EAlertLevel(Enum):
    UNAWARE = 0
    ALERTED = 1
    LKP = 2
    THREATENED = 3
    COUNT = 4
    EAlertLevel_MAX = 5


class EAthenaGamePhase(Enum):
    NONE = 0
    SETUP = 1
    WARMUP = 2
    AIRCRAFT = 3
    SAFE_ZONES = 4
    END_GAME = 5
    COUNT = 6
    EAthenaGamePhase_MAX = 7


class EAthenaStormCapState(Enum):
    NONE = 0
    CLEAR = 1
    WARNING = 2
    DAMAGING = 3
    COUNT = 4
    EAthenaStormCapState_MAX = 5


class EDeathCause(Enum):
    OUTSIDE_SAFE_ZONE = 0
    FALL_DAMAGE = 1
    PISTOL = 2
    SHOTGUN = 3
    RIFLE = 4
    SMG = 5
    SNIPER = 6
    SNIPER_NO_SCOPE = 7
    MELEE = 8
    InfinityBlade = 9
    GRENADE = 10
    C4 = 11
    GRENADE_LAUNCHER = 12
    ROCKET_LAUNCHER = 13
    MINIGUN = 14
    BOW = 15
    TRAP = 16
    DBNO_TIMEOUT = 17
    BANHAMMER = 18
    REMOVED_FROM_GAME = 19
    MASSIVE_MELEE = 20
    MASSIVE_DIVE_BOMB = 21
    MASSIVE_RANGED = 22
    VEHICLE = 23
    SHOPPING_CART = 24
    ATK = 25
    QUAD_CRASHER = 26
    BIPLANE = 27
    BIPLANE_GUN = 28
    LMG = 29
    GAS_GRENADE = 30
    INSTANT_ENVIRONMENTAL = 31
    INSTANT_ENVIRONMENTAL_FELL_OUT_OF_WORLD = 32
    INSTANT_ENVIRONMENTAL_UNDER_LANDSCAPE = 33
    TURRET = 34
    SHIP_CANNON = 35
    CUBE = 36
    BALLOON = 37
    STORM_SURGE = 38
    LAVA = 39
    BASIC_FIEND = 40
    ELITE_FIEND = 41
    RANGED_FIEND = 42
    BASIC_BRUTE = 43
    ELITE_BRUTE = 44
    MEGA_BRUTE = 45
    SILENT_SWITCHING_TO_SPECTATE = 46
    LOGGED_OUT = 47
    TEAM_SWITCH_SUICIDE = 48
    WON_MATCH = 49
    UNSPECIFIED = 50
    COUNT = 51
    EDeathCause_MAX = 52


class EEventTournamentRound(Enum):
    OPEN = 0
    QUALIFIERS = 1
    SEMI_FINALS = 2
    FINALS = 3
    UNKNOWN = 4
    ARENA = 5
    COUNT = 6
    EEventTournamentRound_MAX = 7


class EFortBuildingState(Enum):
    PLACEMENT = 0
    EDIT_MODE = 1
    NONE = 2
    COUNT = 3
    EFortBuildingState_MAX = 4


class EFortGameplayState(Enum):
    NORMAL_GAMEPLAY = 0
    WAITING_TO_START = 1
    END_OF_ZONE = 2
    ENTERING_ZONE = 3
    LEAVING_ZONE = 4
    INVALID = 5
    COUNT = 6
    EFortGameplayState_MAX = 7


class EFortMovementStyle(Enum):
    RUNNING = 0
    WALKING = 1
    CHARGING = 2
    SPRINTING = 3
    PERSONAL_VEHICLE = 4
    FLYING = 5
    TETHERED = 6
    BURROWING = 7
    COUNT = 8
    EFortMovementStyle_MAX = 9


class EFortPickupTossState(Enum):
    NOT_TOSSED = 0
    IN_PROGRESS = 1
    AT_REST = 2
    COUNT = 3
    EFortPickupTossState_MAX = 4


class EFortWeaponType(Enum):
    NONE = 0
    RANGED_ANY = 1
    PISTOL = 2
    SHOTGUN = 3
    RIFLE = 4
    SMG = 5
    SNIPER = 6
    GRENADE_LAUNCHER = 7
    ROCKET_LAUNCHER = 8
    BOW = 9
    MINIGUN = 10
    LMG = 11
    BIPLANE_GUN = 12
    MELEE_ANY = 13
    HARVESTING_TOOL = 14
    COUNT = 15
    MAX = 16


class ENetRole(Enum):
    ROLE_NONE = 0
    ROLE_SIMULATED_PROXY = 1
    ROLE_AUTONOMOUS_PROXY = 2
    ROLE_AUTHORITY = 3
    COUNT = 4
    ROLE_MAX = 5


class EServerStability(Enum):
    STABLE = 0
    LOW_INSTABILITY = 1
    HIGH_INSTABILITY = 2
    COUNT = 3
    EServerStability_MAX = 4
