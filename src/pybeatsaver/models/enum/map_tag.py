from .human_enum import HumanEnum
from .map_tag_type import EMapTagType


class EMapTag(HumanEnum):
    NONE = (EMapTagType.NONE, "", "")

    TECH = (EMapTagType.STYLE, "Tech", "tech")
    DANCESTYLE = (EMapTagType.STYLE, "Dance", "dance-style")
    SPEED = (EMapTagType.STYLE, "Speed", "speed")
    BALANCED = (EMapTagType.STYLE, "Balanced", "balanced")
    CHALLENGE = (EMapTagType.STYLE, "Challenge", "challenge")
    ACCURACY = (EMapTagType.STYLE, "Accuracy", "accuracy")
    FITNESS = (EMapTagType.STYLE, "Fitness", "fitness")

    SWING = (EMapTagType.GENRE, "Swing", "swing")
    NIGHTCORE = (EMapTagType.GENRE, "Nightcore", "nightcore")
    FOLK = (EMapTagType.GENRE, "Folk & Acoustic", "folk-acoustic")
    FAMILY = (EMapTagType.GENRE, "Kids & Family", "kids-family")
    AMBIENT = (EMapTagType.GENRE, "Ambient", "ambient")
    FUNK = (EMapTagType.GENRE, "Funk & Disco", "funk-disco")
    JAZZ = (EMapTagType.GENRE, "Jazz", "jazz")
    CLASSICAL = (EMapTagType.GENRE, "Classical & Orchestral", "classical-orchestral")
    SOUL = (EMapTagType.GENRE, "Soul", "soul")
    SPEEDCORE = (EMapTagType.GENRE, "Speedcore", "speedcore")
    PUNK = (EMapTagType.GENRE, "Punk", "punk")
    RB = (EMapTagType.GENRE, "R&B", "rb")
    HOLIDAY = (EMapTagType.GENRE, "Holiday", "holiday")
    VOCALOID = (EMapTagType.GENRE, "Vocaloid", "vocaloid")
    JROCK = (EMapTagType.GENRE, "J-Rock", "j-rock")
    TRANCE = (EMapTagType.GENRE, "Trance", "trance")
    DRUMBASS = (EMapTagType.GENRE, "Drum and Bass", "drum-and-bass")
    COMEDY = (EMapTagType.GENRE, "Comedy & Meme", "comedy-meme")
    INSTRUMENTAL = (EMapTagType.GENRE, "Instrumental", "instrumental")
    HARDCORE = (EMapTagType.GENRE, "Hardcore", "hardcore")
    KPOP = (EMapTagType.GENRE, "K-Pop", "k-pop")
    INDIE = (EMapTagType.GENRE, "Indie", "indie")
    TECHNO = (EMapTagType.GENRE, "Techno", "techno")
    HOUSE = (EMapTagType.GENRE, "House", "house")
    GAME = (EMapTagType.GENRE, "Video Game", "video-game-soundtrack")
    FILM = (EMapTagType.GENRE, "TV & Film", "tv-movie-soundtrack")
    ALT = (EMapTagType.GENRE, "Alternative", "alternative")
    DUBSTEP = (EMapTagType.GENRE, "Dubstep", "dubstep")
    METAL = (EMapTagType.GENRE, "Metal", "metal")
    ANIME = (EMapTagType.GENRE, "Anime", "anime")
    HIPHOP = (EMapTagType.GENRE, "Hip Hop & Rap", "hip-hop-rap")
    JPOP = (EMapTagType.GENRE, "J-Pop", "j-pop")
    DANCE = (EMapTagType.GENRE, "Dance", "dance")
    ROCK = (EMapTagType.GENRE, "Rock", "rock")
    POP = (EMapTagType.GENRE, "Pop", "pop")
    ELECTRONIC = (EMapTagType.GENRE, "Electronic", "electronic")

    def __new__(cls, tag_type: EMapTagType, human_readable: str, value: str):
        obj = object.__new__(cls)
        obj._tag_type = tag_type
        obj._human_readable = human_readable
        obj._value_ = value
        return obj
    
    @property
    def tag_type(self) -> EMapTagType:
        return self._tag_type