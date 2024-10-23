from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FrutipediaApp.common.helpers import get_user_obj
from FrutipediaApp.fruits.forms import AddFruitForm, EditFruitForm, DeleteFruitForm
from FrutipediaApp.fruits.models import Fruit


class AddFruitView(CreateView):
    model = Fruit
    template_name = 'fruits/create-fruit.html'
    form_class = AddFruitForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class FruitDetailView(DetailView):
    model = Fruit
    template_name = 'fruits/details-fruit.html'
    pk_url_kwarg = 'fruitid'


class FruitEditView(UpdateView):
    model = Fruit
    template_name = 'fruits/edit-fruit.html'
    pk_url_kwarg = 'fruitid'
    form_class = EditFruitForm
    success_url = reverse_lazy('dashboard')


class FruitDeleteView(DeleteView):
    model = Fruit
    template_name = 'fruits/delete-fruit.html'
    pk_url_kwarg = 'fruitid'
    success_url = reverse_lazy('dashboard')
    form_class = DeleteFruitForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
