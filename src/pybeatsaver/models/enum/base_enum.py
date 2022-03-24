from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def has_value(cls, value) -> bool:
        return value in cls._value2member_map_

    @property
    def api_request_value(self) -> str:
        return self.value
