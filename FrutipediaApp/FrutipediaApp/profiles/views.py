from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FrutipediaApp.common.helpers import get_user_obj
from FrutipediaApp.profiles.forms import CreateProfileForm, UpdateProfileForm
from FrutipediaApp.profiles.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profiles/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('dashboard')


class ProfileDetailView(DetailView):
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class EditProfileView(UpdateView):
    template_name = 'profiles/edit-profile.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteProfileView(DeleteView):
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()
