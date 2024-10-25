from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from TastyRecipesApp.common.helpers import get_user_obj
from TastyRecipesApp.profiles.forms import CreateProfileForm, EditProfileForm
from TastyRecipesApp.profiles.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = "profiles/create-profile.html"
    form_class = CreateProfileForm
    success_url = reverse_lazy("catalogue")


class ProfileDetailView(DetailView):
    template_name = "profiles/details-profile.html"

    def get_object(self, queryset=None):
        return get_user_obj()


class EditProfileView(UpdateView):
    template_name = "profiles/edit-profile.html"
    form_class = EditProfileForm
    success_url = reverse_lazy("profile-details")

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteProfileView(DeleteView):
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return get_user_obj()
