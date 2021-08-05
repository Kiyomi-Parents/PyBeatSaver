from dataclasses import dataclass

from dataclasses_json import dataclass_json
from .auth_request import AuthRequest


@dataclass_json
@dataclass
class VoteRequest:
    auth: AuthRequest
    direction: bool
    hash: str
