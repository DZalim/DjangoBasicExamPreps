from django import forms

from TastyRecipesApp.common.mixins import LabelMixin, ReadOnlyMixin
from TastyRecipesApp.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']


class CreateRecipeForm(LabelMixin, RecipeBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "ingredients": "ingredient1, ingredient2, ...",
            "instructions": "Enter detailed instructions here...",
            "image_url": "Optional image URL here..."
        }

        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs["placeholder"] = placeholder


class EditRecipeForm(LabelMixin, RecipeBaseForm):
    pass


class DeleteRecipeForm(LabelMixin, ReadOnlyMixin, RecipeBaseForm):
    readonly_fields = ["title", "cuisine_type", "ingredients", "instructions", "cooking_time", "image_url"]
