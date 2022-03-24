from dataclasses import dataclass
from datetime import datetime
from typing import *

from dataclasses_json import dataclass_json, LetterCase

from .fields import default, datetime_field
from .user_diff_stats import UserDiffStats


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserStats:
    total_upvotes: int = default()
    total_downvotes: int = default()
    total_maps: int = default()
    ranked_maps: int = default()
    avg_bpm: float = default()
    avg_score: float = default()
    avg_duration: float = default()
    first_upload: Optional[datetime] = datetime_field()
    last_upload: Optional[datetime] = datetime_field()
    diff_stats: Optional[UserDiffStats] = default()
