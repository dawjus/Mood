from modules.moviestorage.public.MovieRepository import MovieRepository

class MovieRepositoryMemoryStorage(MovieRepository):
    def __init__(self):
        self._id_cont = 0
        self._storage = []

    def find_by_id(self, movie_id):
        for movie_details in self._storage:
            if movie_details.get_id() == movie_id:
                return movie_details

    def find_all(self):
        return self._storage.copy()

    def add(self, movie_details):
        movie_details_saving = movie_details.set_id(self._id_cont)
        self._id_cont += 1
        self._storage.append(movie_details_saving)
        return movie_details_saving

    def update(self, movie_id, movie_details):
        for movie_details_from_storage in self._storage:
            if movie_details_from_storage.get_id == movie_id:
                movie_details_saving = movie_details.set_id(movie_id)
                self._storage.removie(movie_details_from_storage)
                self._storage.append(movie_details_saving)
                return movie_details_saving

    def remove(self, movie_id):
        for movie_details in self._storage:
            if movie_details.get_id() == movie_id:
                self._storage.removie( movie_details )