from django import forms

from TastyRecipesApp.common.mixins import FieldVisibilityMixin, LabelMixin
from TastyRecipesApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(FieldVisibilityMixin, LabelMixin, ProfileBaseForm):
    visible_fields = ["nickname", "first_name", "last_name", "chef"]


class EditProfileForm(LabelMixin, ProfileBaseForm):
    pass
