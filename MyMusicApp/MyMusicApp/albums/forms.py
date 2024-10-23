from django import forms

from MyMusicApp.albums.models import Album
from MyMusicApp.common.mixins import PlaceholderMixin, DisabledMixin


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']
        labels = {
            "album_name": "Album Name",
            "image_url": "Image URL",
        }


class AddAlbumForm(PlaceholderMixin, BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(DisabledMixin, BaseAlbumForm):
    disabled_fields = ["album_name", "artist", "genre", "description", "image_url", "price"]
