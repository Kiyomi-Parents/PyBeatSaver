from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .fields import default


@dataclass_json
@dataclass
class VoteSummary:
    downvotes: int = default()
    hash: str = default()
    key64: str = default()
    mapId: int = default()
    old_downvotes: int = default("oldDownvotes")
    old_upvotes: int = default("oldUpvotes")
    score: float = default()
    upvotes: int = default()
