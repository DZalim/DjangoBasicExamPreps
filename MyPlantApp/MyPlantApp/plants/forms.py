from django import forms

from MyPlantApp.common.mixins import DisabledMixin
from MyPlantApp.plants.models import Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ['owner']

        labels = {
            'plant_type': 'Type',
            'image_url': 'Image URL',
        }


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(DisabledMixin, PlantBaseForm):
    disabled_fields = ['plant_type', 'name', 'image_url', 'description', 'price']
