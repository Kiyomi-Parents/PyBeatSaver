from dataclasses import dataclass
from typing import *

from dataclasses_json import dataclass_json, LetterCase

from .enum import EAccountType
from .fields import default, enum_field
from .user_stats import UserStats


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserDetail:
    id: int = default()
    name: str = default()
    unique_set: Optional[bool] = default()
    hash: Optional[str] = default()
    testplay: Optional[bool] = default()
    avatar: str = default()
    stats: Optional[UserStats] = default()
    type: EAccountType = enum_field(EAccountType)
    email: Optional[str] = default()
    upload_limit: Optional[int] = default()
    curator: Optional[bool] = default()
