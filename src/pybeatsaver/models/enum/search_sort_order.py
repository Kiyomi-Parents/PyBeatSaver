from .base_enum import BaseEnum


class ESearchSortOrder(BaseEnum):
    LATEST = "Latest"
    RELEVANCE = "Relevance"
    RATING = "Rating",
    CURATED = "Curated"

    @staticmethod
    def deserialize(value: str):
        return ESearchSortOrder(value)

    @property
    def serialize(self) -> str:
        return self.value

