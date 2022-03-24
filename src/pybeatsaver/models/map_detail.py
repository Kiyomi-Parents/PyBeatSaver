from dataclasses import dataclass
from datetime import datetime
from typing import *

from dataclasses_json import dataclass_json, LetterCase

from .fields import default, datetime_field, enum_field
from .map_detail_metadata import MapDetailMetadata
from .map_stats import MapStats
from .map_version import MapVersion
from .user_detail import UserDetail
from .enum import EMapTag


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class MapDetail:
    id: str = default()
    name: str = default()
    description: str = default()
    uploader: UserDetail = default()
    metadata: MapDetailMetadata = default()
    stats: MapStats = default()
    automapper: bool = default()
    ranked: bool = default()
    qualified: bool = default()
    versions: List[MapVersion] = default()
    curator: Optional[UserDetail] = default()
    tags: Optional[List[EMapTag]] = enum_field(EMapTag)
    created_at: datetime = datetime_field()
    curated_at: Optional[datetime] = datetime_field()
    updated_at: datetime = datetime_field()
    deleted_at: Optional[datetime] = datetime_field()
    uploaded: Optional[datetime] = datetime_field()
    last_published_at: Optional[datetime] = datetime_field()
