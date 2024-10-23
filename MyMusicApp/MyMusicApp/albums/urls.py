from django.urls import path, include

from MyMusicApp.albums.views import AddAlbumView, AlbumDetailView, AlbumEditView, AlbumDeleteView

urlpatterns = [
    path('add/', AddAlbumView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('details/', AlbumDetailView.as_view(), name='album-details'),
        path('edit', AlbumEditView.as_view(), name='album-edit'),
        path('delete/', AlbumDeleteView.as_view(), name='album-delete'),
    ]))
]
