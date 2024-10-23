from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from MyMusicApp.albums.models import Album
from MyMusicApp.common.helpers import get_user_obj
from MyMusicApp.profiles.forms import ProfileCreateForm


class HomeView(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_obj()

        if profile:
            return ['home-with-profile.html']

        return ['home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
