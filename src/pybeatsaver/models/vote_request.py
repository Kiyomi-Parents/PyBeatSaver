from dataclasses import dataclass

from dataclasses_json import dataclass_json
from .auth_request import AuthRequest
from .fields import default


@dataclass_json
@dataclass
class VoteRequest:
    auth: AuthRequest = default()
    direction: bool = default()
    hash: str = default()
