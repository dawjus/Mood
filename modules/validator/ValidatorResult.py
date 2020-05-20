from abc import ABC, abstractmethod


class ValidatorResult(ABC):
    @abstractmethod
    def is_valid(self):
        raise

    def get_error(self):
        raise
