from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json
from .user_stats import UserStats


@dataclass_json
@dataclass
class UserDetail:
    avatar: str
    hash: str
    id: int
    name: str
    stats: Optional[UserStats] = None
    testplay: Optional[bool] = None

