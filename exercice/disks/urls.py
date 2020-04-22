from django.urls import path
from . import views

urlpatterns = [
    path('', views.tous_albums, name = "tousAlbums"),
    path('detailsAlbum', views.details_album, name = "detailsAlbum")
]