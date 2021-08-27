from dataclasses import dataclass
from datetime import datetime
from typing import *

from dataclasses_json import dataclass_json

from .fields import default, datetime_field
from .user_diff_stats import UserDiffStats


@dataclass_json
@dataclass
class UserStats:
    total_upvotes: int = default("totalUpvotes")
    total_downvotes: int = default("totalDownvotes")
    total_maps: int = default("totalMaps")
    ranked_maps: int = default("rankedMaps")
    avg_bpm: float = default("avgBpm")
    avg_score: float = default("avgScore")
    avg_duration: float = default("avgDuration")
    first_upload: Optional[datetime] = datetime_field("firstUpload")
    last_upload: Optional[datetime] = datetime_field("lastUpload")
    diff_stats: Optional[UserDiffStats] = default("diffStats")
