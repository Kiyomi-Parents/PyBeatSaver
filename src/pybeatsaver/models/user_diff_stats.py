from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .fields import default


@dataclass_json
@dataclass
class UserDiffStats:
    easy: int = default()
    expert: int = default()
    expert_plus: int = default("expertPlus")
    hard: int = default()
    normal: int = default()
    total: int = default()
