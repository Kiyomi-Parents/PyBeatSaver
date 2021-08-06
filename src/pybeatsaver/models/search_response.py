from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from .fields import default
from .map_detail import MapDetail
from .user_detail import UserDetail


@dataclass_json
@dataclass
class SearchResponse:
    docs: List[MapDetail] = default()
    redirect: str = default()
    user: UserDetail = default()
