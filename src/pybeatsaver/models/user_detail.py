from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from .fields import default
from .user_stats import UserStats


@dataclass_json
@dataclass
class UserDetail:
    avatar: str = default()
    hash: str = default()
    id: int = default()
    name: str = default()
    stats: Optional[UserStats] = default()
    testplay: Optional[bool] = default()

