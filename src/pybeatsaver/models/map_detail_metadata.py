from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class MapDetailMetadata:
    bpm: float
    duration: int
    levelAuthorName: str
    songAuthorName: str
    songName: str
    songSubName: str
