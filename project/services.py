from project.settings import BASE_DIR

from modules.moviestorage.public.MovieStorageService import MovieStorageService
from modules.moviestorage.public.repositories.MovieRepositoryImdbJson import MovieRepositoryImdbJson

from modules.movierating.public.MovieRatingService import MovieRatingService
from modules.movierating.public.repositories.MovieRatingRepositoryMemoryStorage import MovieRatingRepositoryMemoryStorage


def _init_movie_storage_service():
    print("Create movie storage service...")
    repository = MovieRepositoryImdbJson(BASE_DIR+'\\templates\\MovieDatabase.json')
    return MovieStorageService(repository)


def _init_movie_rating_service():
    print("Create movie rating service...")
    return MovieRatingService(MovieRatingRepositoryMemoryStorage())


MOVIE_STORAGE_SERVICE = _init_movie_storage_service()
MOVIE_RATING_SERVICE = _init_movie_rating_service()