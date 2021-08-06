from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json

from .fields import datetime_field, default
from .user_detail import UserDetail


@dataclass_json
@dataclass
class MapTestplay:
    created_at: datetime = datetime_field("createdAt")
    feedback: str = default()
    feedback_at: datetime = datetime_field("feedbackAt")
    user: UserDetail = default()
    video: str = default()
