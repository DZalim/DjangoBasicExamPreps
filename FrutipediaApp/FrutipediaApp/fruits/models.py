from django.core.validators import MinLengthValidator
from django.db import models

from FrutipediaApp.fruits.validators import OnlyLetterValidator


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(2),
            OnlyLetterValidator(),
        ],
        error_messages={
            'unique': "This fruit name is already in use! Try a new one.",
        }
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='fruits',
    )
