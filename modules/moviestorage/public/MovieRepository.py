from abc import ABC, abstractmethod

class MovieRepository(ABC):
    # Return MovieDetails or null
    @abstractmethod
    def find_by_id(self, movie_id):
        raise Exception("Not implemented")

    # Return all MovieDetails
    @abstractmethod
    def find_all(self):
        raise Exception("Not implemented")

    # Add MovieDetails with new id
    # Return saved MovieDetails
    @abstractmethod
    def add(self, movie_details):
        raise Exception("Not implemented")

    # Replace exist MovieDetails with current movie_id
    # Return saved MovieDetails
    @abstractmethod
    def update(self, movie_id, movie_details):
        raise Exception("Not implemented")

    # Remove MovieDetails with current movie_id
    # Return nothing
    @abstractmethod
    def remove(self, movie_id):
        raise Exception("Not implemented")

