from dataclasses import dataclass
from typing import *

from dataclasses_json import dataclass_json

from .fields import default
from .map_detail import MapDetail


@dataclass_json
@dataclass
class SearchInfo:
    duration: float = default()
    pages: int = default()
    total: int = default()

@dataclass_json
@dataclass
class SearchResponse:
    docs: Optional[List[MapDetail]] = default()
    info: Optional[SearchInfo] = default()
    redirect: Optional[str] = default()
