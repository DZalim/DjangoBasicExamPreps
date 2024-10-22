from django.urls import path

from MyPlantApp.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),

]