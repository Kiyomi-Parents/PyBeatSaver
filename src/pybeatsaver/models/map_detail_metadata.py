from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from .fields import default


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class MapDetailMetadata:
    bpm: float = default()
    duration: int = default()
    song_name: str = default()
    song_sub_name: str = default()
    song_author_name: str = default()
    level_author_name: str = default()
