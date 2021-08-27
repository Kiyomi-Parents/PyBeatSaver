from dataclasses import dataclass
from datetime import datetime
from typing import *

from dataclasses_json import dataclass_json

from .fields import datetime_field, default
from .map_difficulty import MapDifficulty
from .enum.map_state import MapState
from .map_testplay import MapTestplay


@dataclass_json
@dataclass
class MapVersion:
    hash: str = default()
    key: Optional[str] = default()
    state: MapState = default()
    created_at: datetime = datetime_field("createdAt")
    sage_score: Optional[int] = default("sageScore")
    diffs: List[MapDifficulty] = default()
    feedback: Optional[str] = default()
    testplay_at: Optional[datetime] = datetime_field("testplayAt")
    testplays: Optional[List[MapTestplay]] = default()
    download_url: str = default("downloadURL")
    cover_url: str = default("coverURL")
    preview_url: str = default("previewURL")
