from django.urls import path, include

from FurryFunniesAppRegularExam.posts import views

urlpatterns = [
    path("create/", views.CreatePostView.as_view(), name="create-post"),
    path("<int:post_id>/", include([
        path("details/", views.PostDetailsView.as_view(), name="post-details"),
        path("edit/", views.EditPostView.as_view(), name="edit-post"),
        path("delete/", views.DeletePostView.as_view(), name="delete-post"),
    ])),
]
