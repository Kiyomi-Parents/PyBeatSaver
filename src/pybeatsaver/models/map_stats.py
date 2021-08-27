from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .fields import default


@dataclass_json
@dataclass
class MapStats:
    plays: int = default()
    downloads: int = default()
    upvotes: int = default()
    downvotes: int = default()
    score: float = default()
