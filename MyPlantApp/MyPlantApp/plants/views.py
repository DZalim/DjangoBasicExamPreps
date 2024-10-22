from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from MyPlantApp.common.helpers import get_user_obj
from MyPlantApp.plants.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from MyPlantApp.plants.models import Plant


class CreatePlantView(CreateView):
    model = Plant
    template_name = 'plants/create-plant.html'
    form_class = PlantCreateForm
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class PlantDetailView(DetailView):
    model = Plant
    template_name = 'plants/plant-details.html'


class EditPlantView(UpdateView):
    model = Plant
    template_name = 'plants/edit-plant.html'
    success_url = reverse_lazy('catalogue')
    form_class = PlantEditForm


class DeletePlantView(DeleteView):
    model = Plant
    template_name = 'plants/delete-plant.html'
    success_url = reverse_lazy('catalogue')
    form_class = PlantDeleteForm

    def get_initial(self):
        return self.object.__dict__

    def get_form_kwargs(self):  # Submits the data to the delete form
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial()
        })

        return kwargs
