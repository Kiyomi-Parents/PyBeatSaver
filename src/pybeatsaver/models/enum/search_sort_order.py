from enum import Enum


class ESearchSortOrder(Enum):
    LATEST = "Latest"
    RELEVANCE = "Relevance"
    RATING = "Rating"
    CURATED = "Curated"
    RANDOM = "Random"
