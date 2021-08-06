from dataclasses import dataclass

from dataclasses_json import dataclass_json

from src.pybeatsaver.models.fields import default


@dataclass_json
@dataclass
class AuthRequest:
    oculus_id: str = default("oculusId")
    proof: str = default()
    steam_id: str = default("steamId")
