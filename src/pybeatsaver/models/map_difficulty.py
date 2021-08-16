from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from .enum.characteristic import Characteristic
from .enum.difficulty import Difficulty
from .fields import default, characteristic_field, difficulty_field
from .map_parity_summary import MapParitySummary


@dataclass_json
@dataclass
class MapDifficulty:
    bombs: int = default()
    characteristic: Characteristic = characteristic_field()
    chroma: bool = default()
    cinema: bool = default()
    difficulty: Difficulty = difficulty_field()
    events: int = default()
    length: float = default()
    me: bool = default()
    ne: bool = default()
    njs: float = default()
    notes: int = default()
    nps: int = default()
    obstacles: int = default()
    offset: float = default()
    parity_summary: MapParitySummary = default("paritySummary")
    seconds: float = default()
    stars: Optional[float] = default()
