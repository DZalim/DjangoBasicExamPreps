from django import forms

from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.common.mixins import ReadOnlyMixin, DisabledMixin


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ["owner"]

        labels = {
            "image_url": "Image URL",
        }

        widgets = {
            "image_url": forms.URLInput(
                attrs={
                    "placeholder": "https://..."
                }
            ),
        }


class CreateCarForm(BaseCarForm):
    pass


class UpdateCarForm(BaseCarForm):
    pass


class DeleteCarForm(ReadOnlyMixin, DisabledMixin, BaseCarForm):
    readonly_fields = ["type", "model", "year", "image_url", "price"]
    disabled_fields = ["type", "model", "year", "image_url", "price"]
