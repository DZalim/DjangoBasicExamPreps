from django.urls import path

from TastyRecipesApp.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
