class MovieWithRating:
    def __init__(self, user_id, movie_id, rating):
        self._user_id = user_id
        self._move_id = movie_id
        self.rating = rating

    def copy(self):
        return MovieWithRating(self._user_id, self._move_id, self._movie_rating)

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, user_id):
        copy = self.copy();
        copy._user_id = user_id
        return copy

    def get_movie_id(self):
        return self._move_id

    def set_movie_id(self, movie_id):
        copy = self.copy()
        copy._move_id = movie_id
        return copy

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        copy = self.copy()
        copy._rating = rating
        return copy
