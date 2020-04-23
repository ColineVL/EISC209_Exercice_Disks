from django.urls import path
from . import views

urlpatterns = [
    # TODO ajouter une vue pour créer et ajouter un album à la base
    path('', views.tous_albums, name="tousAlbums"),
    path('detailsAlbum/<int:id>-<str:title>', views.details_album, name="detailsAlbum"),
    path('recherche', views.recherche, name='recherche'),



]
