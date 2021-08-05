from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import dataclass_json, config
from dateutil import parser
from marshmallow import fields

from .user_diff_stats import UserDiffStats


@dataclass_json
@dataclass
class UserStats:
    avgBpm: float
    avgDuration: float
    avgScore: float
    diffStats: UserDiffStats
    firstUpload: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=parser.isoparse,
            mm_field=fields.DateTime(format='iso')
        )
    )
    lastUpload: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=parser.isoparse,
            mm_field=fields.DateTime(format='iso')
        )
    )
    rankedMaps: int
    totalDownvotes: int
    totalMaps: int
    totalUpvotes: int
