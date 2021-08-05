from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class UserDiffStats:
    easy: int
    expert: int
    expertPlus: int
    hard: int
    normal: int
    total: int
