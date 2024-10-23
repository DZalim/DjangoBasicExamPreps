from django import forms

from FrutipediaApp.common.mixins import NoLabelMixin, PlaceholderMixin, FieldVisibilityMixin, LabelMixin
from FrutipediaApp.profiles.models import Profile


class BaseProfileForm(LabelMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'image_url': "Image URL",
        }


class CreateProfileForm(FieldVisibilityMixin, NoLabelMixin, PlaceholderMixin, BaseProfileForm):
    visible_fields = ['first_name', 'last_name', 'email', 'password']


class UpdateProfileForm(FieldVisibilityMixin, BaseProfileForm):
    visible_fields = ['first_name', 'last_name', 'image_url', 'age']
