from abc import ABC, abstractmethod


class MovieRatingRepository(ABC):
    @abstractmethod
    def find_by_user_and_by_movie_id(self, user_id, movie_id):
        pass

    @abstractmethod
    def find_all_by_user(self, user_id):
        pass

    @abstractmethod
    def save(self, rated_movie):
        pass

    @abstractmethod
    def delete_by_user_and_by_movie(self, user_id, movie_id):
        pass

    @abstractmethod
    def delete_all_by_user(self, user_id):
        pass

    @abstractmethod
    def delete_all_by_movie_id(self, movie_id):
        pass