from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from WorldOfSpeedApp.cars.forms import CreateCarForm, UpdateCarForm, DeleteCarForm
from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.common.helpers import get_user_obj


class CarCatalogueView(ListView):
    model = Car
    template_name = "cars/catalogue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_obj()
        context['cars'] = context['profile'].cars.all()

        return context


class CarCreateView(CreateView):
    model = Car
    template_name = "cars/car-create.html"
    form_class = CreateCarForm
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = "cars/car-details.html"


class CarEditView(UpdateView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = "cars/car-edit.html"
    success_url = reverse_lazy('catalogue')
    form_class = UpdateCarForm


class CarDeleteView(DeleteView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = "cars/car-delete.html"
    success_url = reverse_lazy('catalogue')
    form_class = DeleteCarForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
