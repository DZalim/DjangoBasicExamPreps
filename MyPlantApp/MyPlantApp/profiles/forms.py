from django import forms

from MyPlantApp.common.mixins import LabelMixin
from MyPlantApp.profiles.models import Profile


class ProfileBaseForm(LabelMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(LabelMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_picture', ]


class ProfileEditForm(ProfileBaseForm):
    pass
