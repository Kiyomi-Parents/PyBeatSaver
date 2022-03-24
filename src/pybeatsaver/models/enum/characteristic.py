from .human_enum import HumanEnum


class ECharacteristic(HumanEnum):
    STANDARD = ("Standard", "Standard")
    ONE_SABER = ("OneSaber", "One Saber")
    NO_ARROWS = ("NoArrows", "No Arrows")
    DEGREE_90 = ("_90Degree", "90 Degree")
    DEGREE_360 = ("_360Degree", "360 Degree")
    LIGHTSHOW = ("Lightshow", "Lightshow")
    LAWLESS = ("Lawless", "Lawless")

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in [class_value[0].replace("_", "") for class_value in cls.get_class_values()]

    @staticmethod
    def deserialize(value: str):
        value = value.replace("_", "")

        for class_value in ECharacteristic.get_class_values():
            if class_value[0].replace("_", "") == value:
                return ECharacteristic(class_value)

    @property
    def serialize(self) -> str:
        return self.value[0].replace("_", "")

    @property
    def human_readable(self) -> str:
        return self.value[1]


