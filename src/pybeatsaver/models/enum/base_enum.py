from abc import abstractmethod
from enum import Enum
from typing import List


class BaseEnum(Enum):
    @classmethod
    def get_class_values(cls) -> List[str]:
        return [cls_value for cls_value in cls._value2member_map_]

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls.get_class_values()

    @staticmethod
    @abstractmethod
    def deserialize(value: str):
        pass

    @property
    def serialize(self) -> str:
        return self.value[2]

    def __str__(self) -> str:
        return self.serialize
