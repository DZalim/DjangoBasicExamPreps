from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class BetweenYearValidator:
    def __init__(self, start_year=1999, end_year=2030, message=None):
        self.start_year = start_year
        self.end_year = end_year
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"Year must be between {self.start_year} and {self.end_year}!"
        else:
            self.__message = value

    def __call__(self, value: int, *args, **kwargs):
        if not self.start_year <= value <= self.end_year:
            raise ValidationError(self.message)
