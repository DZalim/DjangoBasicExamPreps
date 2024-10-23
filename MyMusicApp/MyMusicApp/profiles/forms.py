from django import forms

from MyMusicApp.common.mixins import PlaceholderMixin
from MyMusicApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(PlaceholderMixin, ProfileBaseForm):
    pass
