from .human_enum import HumanEnum


class EDifficulty(HumanEnum):
    EASY = (1, "Easy", "Easy")
    NORMAL = (3, "Normal", "Normal")
    HARD = (5, "Hard", "Hard")
    EXPERT = (7, "Expert", "Expert")
    EXPERT_PLUS = (9, "Expert+", "ExpertPlus")

    def __new__(cls, difficulty_int: int, human_readable: str, value: str):
        obj = object.__new__(cls)
        obj._human_readable = human_readable
        obj._difficulty_int = difficulty_int
        obj._value_ = value
        return obj

    @property
    def difficulty_int(self) -> int:
        return self._difficulty_int
