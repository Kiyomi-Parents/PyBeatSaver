from dataclasses import dataclass

from dataclasses_json import dataclass_json

from .fields import default


@dataclass_json
@dataclass
class MapDetailMetadata:
    bpm: float = default()
    duration: int = default()
    level_author_name: str = default("levelAuthorName")
    song_author_name: str = default("songAuthorName")
    song_name: str = default("songName")
    song_sub_name: str = default("songSubName")
