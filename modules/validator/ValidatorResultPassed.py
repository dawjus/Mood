from modules.validator.ValidatorResult import ValidatorResult


class ValidatorResultPassed (ValidatorResult):
    def is_valid(self):
        return True
