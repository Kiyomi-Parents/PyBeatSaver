from abc import abstractmethod
from enum import Enum


class HumanEnum(Enum):
    @property
    @abstractmethod
    def human_readable(self) -> str:
        return self._human_readable
