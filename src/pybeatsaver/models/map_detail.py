from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from dataclasses_json import dataclass_json, config
from dateutil import parser
from marshmallow import fields

from .map_detail_metadata import MapDetailMetadata
from .map_stats import MapStats
from .map_version import MapVersion
from .user_detail import UserDetail


@dataclass_json
@dataclass
class MapDetail:
    automapper: bool
    description: str
    id: str
    metadata: MapDetailMetadata
    name: str
    qualified: bool
    ranked: bool
    stats: MapStats
    uploaded: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=parser.isoparse,
            mm_field=fields.DateTime(format='iso')
        )
    )
    uploader: UserDetail
    versions: List[MapVersion]
    curator: Optional[str] = None
