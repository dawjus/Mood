from modules.moviestorage.private.validator.Validator import Validator
from modules.moviestorage.public.MovieRepository import MovieRepository


class MovieStorageService:
    def __init__(self, movie_repository):
        if not isinstance(movie_repository, MovieRepository):
            raise Exception("movie repository is not instance of MovieRepository")
        self._repository = movie_repository

    def get_by_id(self, movie_id):
        return self._repository.find_by_id( movie_id )

    def get_all(self):
        return self._repository.find_all()

    def add(self, movie_details):
        validator_result = Validator().check(movie_details)
        if not validator_result.is_valid():
            raise validator_result.get_error()
        return self._repository.add(movie_details)

    def update(self, movie_id, movie_details):
        validator_result = Validator().check_for_update(movie_details)
        if not validator_result.is_valid():
            raise validator_result.get_error()
        return self._repository.update(movie_id, movie_details)

    def remove(self, movie_id):
        return self._repository.delete(movie_id)
