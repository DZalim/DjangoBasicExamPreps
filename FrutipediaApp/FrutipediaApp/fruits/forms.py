from django import forms

from FrutipediaApp.common.mixins import NoLabelMixin, DisabledMixin, FieldVisibilityMixin
from FrutipediaApp.fruits.models import Fruit


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner']

        labels = {
            'image_url': 'Image URL',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Fruit Name'}
            ),
            'image_url': forms.TextInput(
                attrs={'placeholder': 'Fruit Image URL'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Fruit Description'}
            ),
            'nutrition': forms.Textarea(
                attrs={'placeholder': 'Nutrition Info'}
            )
        }


class AddFruitForm(NoLabelMixin, BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(FieldVisibilityMixin,DisabledMixin, BaseFruitForm):
    visible_fields = ['name', 'image_url', 'description']
    disabled_fields = ['name', 'image_url', 'description']
