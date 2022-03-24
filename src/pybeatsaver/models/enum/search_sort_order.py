from .base_enum import BaseEnum


class ESearchSortOrder(BaseEnum):
    LATEST = "Latest"
    RELEVANCE = "Relevance"
    RATING = "Rating",
    CURATED = "Curated"
