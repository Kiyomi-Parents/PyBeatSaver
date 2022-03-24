from dataclasses import dataclass
from typing import *

from dataclasses_json import dataclass_json

from .enum.characteristic import ECharacteristic
from .enum.difficulty import EDifficulty
from .fields import default, enum_field
from .map_parity_summary import MapParitySummary


@dataclass_json
@dataclass
class MapDifficulty:
    njs: float = default()
    offset: float = default()
    notes: int = default()
    bombs: int = default()
    obstacles: int = default()
    nps: float = default()
    length: float = default()
    characteristic: ECharacteristic = enum_field(ECharacteristic)
    difficulty: EDifficulty = enum_field(EDifficulty)
    events: int = default()
    chroma: bool = default()
    me: bool = default()
    ne: bool = default()
    cinema: bool = default()
    seconds: float = default()
    parity_summary: MapParitySummary = default("paritySummary")
    stars: Optional[float] = default()
