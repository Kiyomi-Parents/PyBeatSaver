from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .fields import default


@dataclass_json
@dataclass
class MapStats:
    downloads: int = default()
    downvotes: int = default()
    plays: int = default()
    score: float = default()
    upvotes: int = default()
