from django.core.validators import MinLengthValidator
from django.db import models

from TastyRecipesApp.profiles.validators import CapitalLetterValidator


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinLengthValidator(2, message="Nickname must be at least 2 chars long!"),
        ],
    )
    first_name = models.CharField(
        max_length=30,
        validators=[
            CapitalLetterValidator(),
        ],
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            CapitalLetterValidator(),
        ],
    )
    chef = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)
