from dataclasses import dataclass
from datetime import datetime
from typing import *

from dataclasses_json import dataclass_json, LetterCase

from .fields import datetime_field, default
from .user_detail import UserDetail


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class MapTestplay:
    feedback: Optional[str] = default()
    video: Optional[str] = default()
    user: UserDetail = default()
    created_at: datetime = datetime_field()
    feedback_at: Optional[datetime] = datetime_field()
