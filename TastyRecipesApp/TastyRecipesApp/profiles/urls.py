from django.urls import path

from TastyRecipesApp.profiles import views

urlpatterns = [
    path("create/", views.CreateProfileView.as_view(), name="create-profile"),
    path("details/", views.ProfileDetailView.as_view(), name="profile-details"),
    path("edit/", views.EditProfileView.as_view(), name="edit-profile"),
    path("delete/", views.DeleteProfileView.as_view(), name="delete-profile"),
]
