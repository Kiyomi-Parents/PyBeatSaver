from .base_enum import BaseEnum


class ELeaderboard(BaseEnum):
    ALL = "All"
    RANKED = "Ranked"
    BEATLEADER = "BeatLeader"
    SCORESABER = "ScoreSaber"

    @staticmethod
    def deserialize(value: str):
        return ELeaderboard(value)

    @property
    def serialize(self) -> str:
        return self.value


