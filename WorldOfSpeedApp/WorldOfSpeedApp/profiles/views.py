from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from WorldOfSpeedApp.common.helpers import get_user_obj
from WorldOfSpeedApp.profiles.forms import ProfileAddForm, ProfileEditForm
from WorldOfSpeedApp.profiles.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = "profiles/profile-create.html"
    form_class = ProfileAddForm
    success_url = reverse_lazy("catalogue")


class ProfileDetailView(DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_price = sum(car.price for car in self.object.cars.all())
        context['total_price'] = total_price

        return context


class EditProfileView(UpdateView):
    template_name = 'profiles/profile-edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy("profile-details")

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteProfileView(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_user_obj()
