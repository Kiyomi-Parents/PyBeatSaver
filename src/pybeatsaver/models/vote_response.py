from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .fields import default


@dataclass_json
@dataclass
class VoteResponse:
    error: str = default()
    success: bool = default()
