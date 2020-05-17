from modules.validator.ValidatorResult import ValidatorResult


class ValidatorResultFailed (ValidatorResult):
    def __init__(self, error_message):
        self.error = error_message

    def is_valid(self):
        return False

    def get_error(self):
        return Exception(self.error)
