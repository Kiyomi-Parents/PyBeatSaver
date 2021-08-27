from dataclasses import dataclass
from datetime import datetime
from typing import *

from dataclasses_json import dataclass_json

from .fields import default, datetime_field
from .map_detail_metadata import MapDetailMetadata
from .map_stats import MapStats
from .map_version import MapVersion
from .user_detail import UserDetail


@dataclass_json
@dataclass
class MapDetail:
    id: str = default()
    name: str = default()
    description: str = default()
    uploader: UserDetail = default()
    metadata: MapDetailMetadata = default()
    stats: MapStats = default()
    uploaded: Optional[datetime] = datetime_field()
    automapper: bool = default()
    ranked: bool = default()
    qualified: bool = default()
    versions: List[MapVersion] = default()
    curator: Optional[str] = default()
    created_at: datetime = datetime_field("createdAt")
    updated_at: datetime = datetime_field("updatedAt")
    last_published_at: Optional[datetime] = datetime_field("lastPublishedAt")
