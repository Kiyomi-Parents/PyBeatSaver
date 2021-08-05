from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import dataclass_json, config
from dateutil import parser
from marshmallow import fields

from .user_detail import UserDetail


@dataclass_json
@dataclass
class MapTestplay:
    createdAt: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=parser.isoparse,
            mm_field=fields.DateTime(format='iso')
        )
    )
    feedback: str
    feedbackAt: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=parser.isoparse,
            mm_field=fields.DateTime(format='iso')
        )
    )
    user: UserDetail
    video: str
