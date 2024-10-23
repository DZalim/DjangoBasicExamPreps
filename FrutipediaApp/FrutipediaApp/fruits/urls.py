from django.urls import path, include

from FrutipediaApp.fruits import views

urlpatterns = [
    path('create/', views.AddFruitView.as_view(), name='add-fruit'),
    path('<int:fruitid>/', include([
        path('details/', views.FruitDetailView.as_view(), name='fruit-details'),
        path('edit/', views.FruitEditView.as_view(), name='fruit-edit'),
        path('delete/', views.FruitDeleteView.as_view(), name='fruit-delete'),
    ])),
]
