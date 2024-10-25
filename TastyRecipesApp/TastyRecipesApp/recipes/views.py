from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from TastyRecipesApp.common.helpers import get_user_obj
from TastyRecipesApp.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from TastyRecipesApp.recipes.models import Recipe


class CatalogueView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = "recipes/catalogue.html"


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = "recipes/create-recipe.html"
    form_class = CreateRecipeForm
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/details-recipe.html"
    pk_url_kwarg = "recipe_id"


class EditRecipeView(UpdateView):
    model = Recipe
    template_name = "recipes/edit-recipe.html"
    form_class = EditRecipeForm
    pk_url_kwarg = "recipe_id"
    success_url = reverse_lazy("catalogue")


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = "recipes/delete-recipe.html"
    form_class = DeleteRecipeForm
    pk_url_kwarg = "recipe_id"
    success_url = reverse_lazy("catalogue")

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
