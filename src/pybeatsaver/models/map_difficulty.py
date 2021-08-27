from dataclasses import dataclass
from typing import *

from dataclasses_json import dataclass_json

from .enum.characteristic import Characteristic
from .enum.difficulty import Difficulty
from .fields import default, characteristic_field, difficulty_field
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
    characteristic: Characteristic = characteristic_field()
    difficulty: Difficulty = difficulty_field()
    events: int = default()
    chroma: bool = default()
    me: bool = default()
    ne: bool = default()
    cinema: bool = default()
    seconds: float = default()
    parity_summary: MapParitySummary = default("paritySummary")
    stars: Optional[float] = default()
