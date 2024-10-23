from django.urls import path

from FrutipediaApp.profiles import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create-profile'),
    path('details/', views.ProfileDetailView.as_view(), name='profile-details'),
    path('edit/', views.EditProfileView.as_view(), name='profile-edit'),
    path('delete/', views.DeleteProfileView.as_view(), name='profile-delete'),

]