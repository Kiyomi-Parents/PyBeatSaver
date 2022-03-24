from dataclasses import dataclass
from datetime import datetime
from typing import *

from dataclasses_json import dataclass_json, LetterCase

from .fields import datetime_field, default
from .map_difficulty import MapDifficulty
from .enum.map_state import EMapState
from .map_testplay import MapTestplay


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class MapVersion:
    hash: str = default()
    key: Optional[str] = default()
    state: EMapState = default()
    created_at: datetime = datetime_field()
    sage_score: Optional[int] = default()
    diffs: List[MapDifficulty] = default()
    feedback: Optional[str] = default()
    testplay_at: Optional[datetime] = datetime_field()
    testplays: Optional[List[MapTestplay]] = default()
    download_url: str = default("downloadURL")
    cover_url: str = default("coverURL")
    preview_url: str = default("previewURL")
    scheduled_at: Optional[datetime] = datetime_field()
