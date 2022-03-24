from .human_enum import HumanEnum


class ECharacteristic(HumanEnum):
    STANDARD = "Standard"
    ONE_SABER = "OneSaber"
    NO_ARROWS = "NoArrows"
    DEGREE_90 = "_90Degree"
    DEGREE_360 = "_360Degree"
    LIGHTSHOW = "Lightshow"
    LAWLESS = "Lawless"

    @staticmethod
    def has_value(value: str) -> bool:
        return value in [class_value.replace("_", "") for class_value in ECharacteristic.get_class_values()]

    @staticmethod
    def deserialize(value: str):
        value = value.replace("_", "")

        for class_value in ECharacteristic.get_class_values():
            if class_value == value:
                return ECharacteristic(class_value)

    @property
    def serialize(self) -> str:
        return self.human_readable

    def get_difficulty_int(self) -> int:
        return self.value[0]

    @property
    def human_readable(self) -> str:
        return self.value.replace("_", "")


