from .human_enum import HumanEnum


class EDifficulty(HumanEnum):
    EASY = (1, "Easy", "Easy")
    NORMAL = (3, "Normal", "Normal")
    HARD = (5, "Hard", "Hard")
    EXPERT = (7, "Expert", "Expert")
    EXPERT_PLUS = (9, "Expert+", "ExpertPlus")

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in [class_value[2] for class_value in EDifficulty.get_class_values()]

    @staticmethod
    def deserialize(value: str):
        for class_value in EDifficulty.get_class_values():
            if class_value[2] == value:
                return EDifficulty(class_value)

    @property
    def serialize(self) -> str:
        return self.get_slug()

    def get_difficulty_int(self) -> int:
        return self.value[0]

    @property
    def human_readable(self) -> str:
        return self.value[1]

    def get_slug(self) -> str:
        return self.value[2]
