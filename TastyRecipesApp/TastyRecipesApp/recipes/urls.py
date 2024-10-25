from django.urls import path, include

from TastyRecipesApp.recipes import views

urlpatterns = [
    path("catalogue/", views.CatalogueView.as_view(), name="catalogue"),
    path("create/", views.CreateRecipeView.as_view(), name="create-recipe"),
    path("<int:recipe_id>/", include([
        path("details/", views.RecipeDetailView.as_view(), name="recipe-details"),
        path("edit/", views.EditRecipeView.as_view(), name="edit-recipe"),
        path("delete/", views.DeleteRecipeView.as_view(), name="delete-recipe"),
    ])),
]
