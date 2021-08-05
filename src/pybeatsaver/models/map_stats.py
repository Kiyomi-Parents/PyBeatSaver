from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class MapStats:
    downloads: int
    downvotes: int
    plays: int
    score: float
    upvotes: int
