from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from .enum.sentiment import ESentiment
from .fields import default, enum_field


@dataclass_json
@dataclass
class MapStats:
    plays: Optional[int] = default()
    downloads: Optional[int] = default()
    upvotes: int = default()
    downvotes: int = default()
    score: float = default()
    reviews: Optional[int] = default()
    sentiment: Optional[ESentiment] = enum_field(ESentiment)
