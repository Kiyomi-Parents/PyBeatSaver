from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json
from .enums.characteristic import Characteristic
from .enums.difficulty import Difficulty
from .map_parity_summary import MapParitySummary


@dataclass_json
@dataclass
class MapDifficulty:
    bombs: int
    characteristic: Characteristic
    chroma: bool
    cinema: bool
    difficulty: Difficulty
    events: int
    length: float
    me: bool
    ne: bool
    njs: float
    notes: int
    nps: int
    obstacles: int
    offset: float
    paritySummary: MapParitySummary
    seconds: float
    stars: Optional[float] = None
