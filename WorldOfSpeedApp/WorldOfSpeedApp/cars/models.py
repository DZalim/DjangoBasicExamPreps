from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WorldOfSpeedApp.cars.choices import CarTypeChoices
from WorldOfSpeedApp.cars.validators import BetweenYearValidator


class Car(models.Model):
    type = models.CharField(max_length=10, choices=CarTypeChoices.choices)
    model = models.CharField(max_length=15, validators=[MinLengthValidator(1), ])
    year = models.IntegerField(validators=[BetweenYearValidator()])
    image_url = models.URLField(
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }
    )
    price = models.FloatField(validators=[MinValueValidator(1.0)])

    owner = models.ForeignKey(
        to="profiles.Profile",
        on_delete=models.CASCADE,
        related_name="cars",
    )
