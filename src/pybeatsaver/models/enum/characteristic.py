from enum import Enum

from .human_enum import HumanEnum

class ECharacteristic(HumanEnum):
    STANDARD = ("Standard", "Standard")
    ONE_SABER = ("OneSaber", "One Saber")
    NO_ARROWS = ("NoArrows", "No Arrows")
    DEGREE_90 = ("90Degree", "90 Degree")
    DEGREE_360 = ("360Degree", "360 Degree")
    LIGHTSHOW = ("Lightshow", "Lightshow")
    LAWLESS = ("Lawless", "Lawless")
    LEGACY = ("Legacy", "Legacy")

    def __new__(cls, value: str, human_readable: str):
        obj = object.__new__(cls)
        obj._value_ = value
        obj._human_readable = human_readable
        return obj
    