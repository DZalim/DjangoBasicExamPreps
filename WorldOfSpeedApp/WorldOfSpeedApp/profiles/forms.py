from django import forms

from WorldOfSpeedApp.common.mixins import FieldVisibilityMixin, LabelMixin
from WorldOfSpeedApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileAddForm(FieldVisibilityMixin, ProfileBaseForm):
    visible_fields = ["username", "email", "age", "password"]


class ProfileEditForm(LabelMixin, ProfileBaseForm):
    pass
