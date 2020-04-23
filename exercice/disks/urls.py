from django.urls import path
from . import views

urlpatterns = [
    # TODO ajouter une vue pour créer et ajouter un album à la base
    # TODO admin
    path('', views.tous_albums, name="tousAlbums"),
    path('detailsAlbum/<int:id>-<str:title>', views.details_album, name="detailsAlbum"),

    path('test', views.test),
    #path('recherche/<str:truc_cherche>', views.recherche, name='recherche'),
    path('recherche', views.recherche, name='recherche'),

]
