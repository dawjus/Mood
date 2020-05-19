from modules.movierating.public.MovieRating import MovieRating


def from_string_to_enum( movie_rating_string):
    if movie_rating_string.lower() == 'like' or movie_rating_string == '1':
        return MovieRating.LIKE
    if movie_rating_string.lower() == 'neutral' or movie_rating_string == '0':
        return MovieRating.NEUTRAL
    if movie_rating_string.lower() == 'unlike' or movie_rating_string == '-1':
        return MovieRating.UNLIKE
    raise Exception("Invalid movie rating value")

def from_enum_to_string(movie_rating_enum):
    if movie_rating_enum == MovieRating.LIKE:
        return 'LIKE'
    if movie_rating_enum == MovieRating.UNLIKE:
        return 'UNLIKE'
    if movie_rating_enum == MovieRating.NEUTRAL:
        return 'NEUTRAL'
    if movie_rating_enum == MovieRating.WAITING_FOR_RATING:
        return 'WAITING_FOR_RATING'
    raise Exception("Invalid movie rating object")