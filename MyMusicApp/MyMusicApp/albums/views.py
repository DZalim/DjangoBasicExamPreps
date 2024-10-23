from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from MyMusicApp.albums.forms import AddAlbumForm, EditAlbumForm, DeleteAlbumForm
from MyMusicApp.albums.models import Album
from MyMusicApp.common.helpers import get_user_obj


class AddAlbumView(CreateView):
    model = Album
    template_name = 'albums/add-album.html'
    success_url = reverse_lazy('home')
    form_class = AddAlbumForm

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'
    pk_url_kwarg = 'id'


class AlbumEditView(UpdateView):
    model = Album
    template_name = 'albums/edit-album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    form_class = EditAlbumForm


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'albums/delete-album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    form_class = DeleteAlbumForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
