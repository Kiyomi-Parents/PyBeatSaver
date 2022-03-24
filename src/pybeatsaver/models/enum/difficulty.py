from .human_enum import HumanEnum


class EDifficulty(HumanEnum):
    EASY = (1, "Easy", "Easy")
    NORMAL = (3, "Normal", "Normal")
    HARD = (5, "Hard", "Hard")
    EXPERT = (7, "Expert", "Expert")
    EXPERT_PLUS = (9, "Expert+", "ExpertPlus")

    def get_difficulty_int(self) -> int:
        return self.value[0]

    def human_readable(self) -> str:
        return self.value[1]

    @property
    def api_request_value(self) -> str:
        return self.value[2]
