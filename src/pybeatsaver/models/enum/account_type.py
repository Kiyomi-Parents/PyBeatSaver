from .base_enum import BaseEnum


class EAccountType(BaseEnum):
    DISCORD = "DISCORD"
    SIMPLE = "SIMPLE"
    DUAL = "DUAL"

    @staticmethod
    def deserialize(value: str):
        for class_value in EAccountType.get_class_values():
            if class_value == value:
                return EAccountType(class_value)
