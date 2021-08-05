from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from dataclasses_json import dataclass_json, config
from dateutil import parser
from marshmallow import fields

from .enums.state import State
from .map_difficulty import MapDifficulty
from .map_testplay import MapTestplay


@dataclass_json
@dataclass
class MapVersion:
    coverURL: str
    createdAt: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=parser.isoparse,
            mm_field=fields.DateTime(format='iso')
        )
    )
    diffs: List[MapDifficulty]
    downloadURL: str
    hash: str
    key: str
    previewURL: str
    sageScore: int
    state: State
    testplayAt: Optional[datetime] = None
    testplays: Optional[List[MapTestplay]] = None
    feedback: Optional[str] = None
