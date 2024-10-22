from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.plants.choices import PlantTypeChoices
from MyPlantApp.plants.validators import OnlyLetterValidator


class Plant(models.Model):
    plant_type = models.CharField(
        max_length=14,
        choices=PlantTypeChoices.choices
    )
    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            OnlyLetterValidator()
        ]
    )
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name="plants",
    )
