from django.urls import path

from FurryFunniesAppRegularExam.authors import views

urlpatterns = [
    path("create/", views.CreateAuthorView.as_view(), name="create-author"),
    path("details/", views.AuthorDetailsView.as_view(), name="author-details"),
    path("edit/", views.EditAuthorView.as_view(), name="edit-author"),
    path("delete/", views.DeleteAuthorView.as_view(), name="delete-author"),
]
