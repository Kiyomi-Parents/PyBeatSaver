from dataclasses import dataclass
from typing import *

from dataclasses_json import dataclass_json

from .enum import AccountType
from .fields import default, account_type_field
from .user_stats import UserStats


@dataclass_json
@dataclass
class UserDetail:
    id: int = default()
    name: str = default()
    unique_set: bool = default("uniqueSet")
    hash: Optional[str] = default()
    testplay: Optional[bool] = default()
    avatar: str = default()
    stats: Optional[UserStats] = default()
    type: AccountType = account_type_field()
