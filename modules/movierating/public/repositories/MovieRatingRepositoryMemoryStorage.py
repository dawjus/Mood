from modules.movierating.public.MovieRatingRepository import MovieRatingRepository


class MovieRatingRepositoryMemoryStorage(MovieRatingRepository):
    def __init__(self):
        self._storage = []

    def find_by_user_and_by_movie_id(self, user_id, movie_id):
        for ratedMovie in self._storage:
            if ratedMovie.get_user_id() == user_id and ratedMovie.get_movie_id() == movie_id:
                return ratedMovie

    def find_all_by_user(self, user_id):
        filtered = []
        for ratedMovie in self._storage:
            if ratedMovie.get_user_id() == user_id:
                filtered.append(ratedMovie)
        return filtered

    def save(self, rated_movie):
        duplicated = self.find_by_user_and_by_movie_id(rated_movie.get_user_id(), rated_movie.get_movie_id())
        if duplicated:
            self._storage.remove(duplicated)
        self._storage.append(rated_movie)

    def delete_by_user_and_by_movie(self, user_id, movie_id):
        finded = self.find_by_user_and_by_movie_id(user_id, movie_id)
        if finded:
            self._storage.remove(finded)

    def delete_all_by_user(self, user_id):
        for ratedMovie in self._storage:
            if ratedMovie.get_user_id() == user_id:
                self._storage.remove(ratedMovie)

    def delete_all_by_movie_id(self, movie_id):
        for ratedMovie in self._storage:
            if ratedMovie.get_movie_id() == movie_id:
                self._storage.remove(ratedMovie)