from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .fields import default


@dataclass_json
@dataclass
class UserDiffStats:
    total: int = default()
    easy: int = default()
    normal: int = default()
    hard: int = default()
    expert: int = default()
    expert_plus: int = default("expertPlus")
