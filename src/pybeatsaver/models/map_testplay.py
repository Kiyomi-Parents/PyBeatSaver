from dataclasses import dataclass
from datetime import datetime
from typing import *

from dataclasses_json import dataclass_json

from .fields import datetime_field, default
from .user_detail import UserDetail


@dataclass_json
@dataclass
class MapTestplay:
    feedback: Optional[str] = default()
    video: Optional[str] = default()
    user: UserDetail = default()
    created_at: datetime = datetime_field("createdAt")
    feedback_at: Optional[datetime] = datetime_field("feedbackAt")
