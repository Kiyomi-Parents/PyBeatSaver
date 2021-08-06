from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json

from .fields import default, datetime_field
from .user_diff_stats import UserDiffStats


@dataclass_json
@dataclass
class UserStats:
    avg_bpm: float = default("avgBpm")
    avg_duration: float = default("avgDuration")
    avg_score: float = default("avgScore")
    diff_stats: UserDiffStats = default("diffStats")
    first_upload: datetime = datetime_field("firstUpload")
    last_upload: datetime = datetime_field("lastUpload")
    ranked_maps: int = default("rankedMaps")
    total_downvotes: int = default("totalDownvotes")
    total_maps: int = default("totalMaps")
    total_upvotes: int = default("totalUpvotes")
