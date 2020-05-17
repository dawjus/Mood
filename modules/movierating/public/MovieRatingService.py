from modules.movierating.private.validator.Validator import Validator
from modules.movierating.public.MovieRating import MovieRating

from modules.movierating.public.MovieRatingRepository import MovieRatingRepository
from modules.movierating.public.MovieWithRating import MovieWithRating


class MovieRatingService:
    def __init__(self, movie_rating_repository):
        if not isinstance(movie_rating_repository, MovieRatingRepository):
            raise Exception( "movie_rating_repository is not instance of MovieRatingRepository")

        self._repository = movie_rating_repository

    def get(self, user_id, movie_id):
        return self._repository.find_by_user_and_by_movie_id(user_id, movie_id)

    def get_all_of_user(self, user_id):
        return self._repository.find_all_by_user(user_id)

    def add_movie_to_rating(self, user_id, movie_id):
        movie_to_rating = MovieWithRating(user_id=user_id, movie_id=movie_id, rating=MovieRating.WAITING_FOR_RATING)
        validator_result = Validator().check(movie_to_rating)
        if not validator_result.is_valid():
            raise validator_result.get_error()
        return self._repository.save(movie_to_rating)

    def rated_by_user(self, rated_movie):
        movie_to_rating = self._repository.find_by_user_and_by_movie_id(rated_movie.get_user_id(),
                                                                        rated_movie.get_movie_id())
        if not movie_to_rating or movie_to_rating.get_rating() != MovieRating.WAITING_FOR_RATING:
            raise Exception("User can not rating this movie!")

        validator_result = Validator().check_for_rating(rated_movie)
        if not validator_result.is_valid():
            raise validator_result.get_error()
        return self._repository.save(rated_movie)

    def remove(self, user_id, movie_id):
        self._repository.delete_by_user_and_by_movie(user_id, movie_id)

    def remove_all_of_user(self, user_id):
        self._repository.delete_all_by_user(user_id)

    def remove_all_of_movie(self, movie_id):
        self._repository.delete_all_by_movie_id(movie_id)