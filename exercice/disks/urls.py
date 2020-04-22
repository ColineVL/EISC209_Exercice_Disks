from django.urls import path
from . import views

urlpatterns = [
    path('', views.tous_albums, name = "tousAlbums"),
    path('detailsAlbum/<int:id>-<str:title>', views.details_album, name = "detailsAlbum"),

    path('test', views.test)
]