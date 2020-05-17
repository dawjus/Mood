import numbers

from modules.validator.ValidatorResultPassed import ValidatorResultPassed
from modules.validator.ValidatorResultFailed import ValidatorResultFailed

from modules.movierating.public.RatedMovie import RatedMovie
from modules.movierating.public.MovieRating import MovieRating


class Validator:
    def check(self, rated_movie):
        if not rated_movie:
            return ValidatorResultFailed("Rated movie not exist")
        if not isinstance(rated_movie, RatedMovie):
            return ValidatorResultFailed("Rated movie is not instance of RatedMovie")

        abnormalities_list = []
        check_user_id_error = self._check_user_id(rated_movie.user_id)
        if check_user_id_error:
            abnormalities_list.append( check_user_id_error )

        check_movie_id_error = self._check_movie_id(rated_movie.move_id)
        if check_movie_id_error:
            abnormalities_list.append(check_user_id_error)

        check_rating_error = self._check_rating(rated_movie.rating)
        if check_rating_error:
            abnormalities_list.append(check_rating_error)
        return self._abnormalities_list_to_validator_result(abnormalities_list)

    def _check_user_id(self, user_id):
        if not user_id:
            return "Invalid user id: Property not exist"
        if not isinstance(user_id, numbers.Number):
            return "Invalid user id: Is not a number"

    def _check_movie_id(self, movie_id):
        if not movie_id:
            return "Invalid movie id: Property not exist"
        if not isinstance(movie_id, numbers.Number):
            return "Invalid movie id: Is not a number"

    def _abnormalities_list_to_validator_result(self, abnormalities_list):
        if len(abnormalities_list) > 0:
            return ValidatorResultFailed( self._abnormalities_list_to_string(abnormalities_list))
        return ValidatorResultPassed()

    def _check_rating(self, movie_rating):
        if not movie_rating:
            return "Invalid movie rating: Property not exist"
        if not isinstance( movie_rating, MovieRating):
            return "Invalid movie rating: Is not instance of MovieRating"


    def _abnormalities_list_to_string(self, abnormalities_list):
        abnormalities_str = "Movie details is incorrect.\n"
        for error in abnormalities_list:
            abnormalities_str += error + "\n"
        return abnormalities_str
