from django.urls import path
from . import views

urlpatterns = [
    path('', views.tous_albums, name = "tousAlbums"),
    path('detailsAlbum/<int:id>-<str:title>', views.details_album, name = "detailsAlbum"),
    #TODO ajouter une vue pour créer et ajouter un album à la base
    #TODO admin


    path('test', views.test)
]