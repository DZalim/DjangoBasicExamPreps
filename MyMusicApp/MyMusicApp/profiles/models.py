from django.core.validators import MinLengthValidator
from django.db import models

from MyMusicApp.profiles.validators import AlphaNumUnderscoreValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumUnderscoreValidator(),
        ]
    )
    email = models.EmailField()
    age = models.PositiveSmallIntegerField(null=True, blank=True)
