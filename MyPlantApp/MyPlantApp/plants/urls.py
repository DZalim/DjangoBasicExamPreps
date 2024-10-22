from django.urls import path

from MyPlantApp.plants import views

urlpatterns = [
    path('create/', views.CreatePlantView.as_view(), name='create-plant'),
    path('details/<int:pk>/', views.PlantDetailView.as_view(), name='plant-details'),
    path('edit/<int:pk>/', views.EditPlantView.as_view(), name='plant-edit'),
    path('delete/<int:pk>/', views.DeletePlantView.as_view(), name='plant-delete'),
]
