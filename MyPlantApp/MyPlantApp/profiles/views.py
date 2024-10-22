from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from MyPlantApp.common.helpers import get_user_obj
from MyPlantApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from MyPlantApp.profiles.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profiles/create-profile.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue')


class ProfileDetailView(DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class EditProfileView(UpdateView):
    template_name = 'profiles/edit-profile.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteProfileView(DeleteView):
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()
