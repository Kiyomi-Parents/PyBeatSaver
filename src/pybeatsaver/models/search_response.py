from dataclasses import dataclass
from typing import *

from dataclasses_json import dataclass_json

from .fields import default
from .map_detail import MapDetail


@dataclass_json
@dataclass
class SearchResponse:
    docs: Optional[List[MapDetail]] = default()
    redirect: Optional[str] = default()
