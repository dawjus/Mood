from modules.movierating.public.MovieRating import MovieRating


def from_string_to_enum( movie_rating_string):
    if movie_rating_string.lower() == 'like' or movie_rating_string == '1':
        return MovieRating.LIKE
    if movie_rating_string.lower() == 'neutral' or movie_rating_string == '0':
        return MovieRating.NEUTRAL
    if movie_rating_string.lower() == 'unlike' or movie_rating_string == '-1':
        return MovieRating.UNLIKE
    raise Exception("Invalid movie rating value")
