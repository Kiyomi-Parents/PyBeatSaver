from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class VoteSummary:
    downvotes: int
    hash: str
    key64: str
    mapId: int
    oldDownvotes: int
    oldUpvotes: int
    score: float
    upvotes: int
