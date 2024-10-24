from django.urls import path, include
from WorldOfSpeedApp.cars import views

urlpatterns = [
    path('catalogue/', views.CarCatalogueView.as_view(), name='catalogue'),
    path('create/', views.CarCreateView.as_view(), name='create-car'),
    path('<int:id>', include([
        path('details/', views.CarDetailView.as_view(), name='car-details'),
        path('edit/', views.CarEditView.as_view(), name='car-edit'),
        path('delete/', views.CarDeleteView.as_view(), name='car-delete'),

    ]))
]