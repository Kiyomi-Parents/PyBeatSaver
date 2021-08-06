from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from dataclasses_json import dataclass_json

from .fields import datetime_field, default
from .map_difficulty import MapDifficulty
from .enums.state import State
from .map_testplay import MapTestplay


@dataclass_json
@dataclass
class MapVersion:
    cover_url: str = default("coverURL")
    created_at: datetime = datetime_field("createdAt")
    diffs: List[MapDifficulty] = default()
    download_url: str = default("downloadURL")
    hash: str = default()
    key: str = default()
    preview_url: str = default("previewURL")
    sage_score: int = default("sageScore")
    state: State = default()
    testplay_at: Optional[datetime] = datetime_field("testplayAt")
    testplays: Optional[List[MapTestplay]] = default()
    feedback: Optional[str] = default()
