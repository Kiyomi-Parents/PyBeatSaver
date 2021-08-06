from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from dataclasses_json import dataclass_json

from .fields import default, datetime_field
from .map_detail_metadata import MapDetailMetadata
from .map_stats import MapStats
from .map_version import MapVersion
from .user_detail import UserDetail


@dataclass_json
@dataclass
class MapDetail:
    automapper: bool = default()
    description: str = default()
    id: str = default()
    metadata: MapDetailMetadata = default()
    name: str = default()
    qualified: bool = default()
    ranked: bool = default()
    stats: MapStats = default()
    uploaded: datetime = datetime_field()
    uploader: UserDetail = default()
    versions: List[MapVersion] = default()
    curator: Optional[str] = default()
