from enum import Enum


class MovieRating (Enum):
    LIKE = 1,
    NEUTRAL = 0,
    UNLIKE = -1,
    WAITING_FOR_RATING = None
