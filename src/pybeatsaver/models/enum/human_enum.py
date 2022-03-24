from abc import abstractmethod

from .base_enum import BaseEnum


class HumanEnum(BaseEnum):
    @property
    @abstractmethod
    def human_readable(self) -> str:
        pass
