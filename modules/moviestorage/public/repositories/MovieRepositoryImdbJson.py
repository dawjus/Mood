import json

from modules.moviestorage.public.MovieRepository import MovieRepository
from modules.moviestorage.public.repositories.MovieRepositoryMemoryStorage import MovieRepositoryMemoryStorage
from modules.moviestorage.public.MovieDetails import MovieDetails


class MovieRepositoryImdbJson(MovieRepository):

    def __init__(self, json_file):
        self._repository_memory_storage = MovieRepositoryMemoryStorage()
        self._read_movie_from_json_file(json_file)

    def find_by_id(self, movie_id):
        return self._repository_memory_storage.find_by_id(movie_id)

    def find_all(self):
        return self._repository_memory_storage.find_all()

    def add(self, movie_details):
        raise Exception("Only read repository")

    def update(self, movie_id, movie_details):
        raise Exception("Only read repository")

    def remove(self, movie_id):
        raise Exception("Only read repository")

    def _read_movie_from_json_file(self, json_file):
        file = open(json_file, "r")
        file_content_json = json.loads(file.read())
        mapper = Mapper()
        for json_object in file_content_json:
            try:
                self._repository_memory_storage.add(mapper.form_json_object_to_movie_details(json_object))
            except Exception:
                print(Exception)

        file.close()


class Mapper:
    def form_json_object_to_movie_details(self, json_object):
        return MovieDetails(name=json_object["title"], description="Unknow", id_move=0, url="https://imdb.com")
