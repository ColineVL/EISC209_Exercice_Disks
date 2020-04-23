from django.shortcuts import render, get_object_or_404

from .models import Album, Artist, Track
from .forms import RechercheForm


# Create your views here.


def tous_albums(request):
    albums = Album.objects.all()
    form = RechercheForm(request.POST or None)

    return render(request, 'disks/tousAlbums.html', locals())


def details_album(request, id, title):
    album = get_object_or_404(Album, id=id)
    listeTracks = album.track_set.all()
    for track in listeTracks:
        duree = int(track.Milliseconds) / 1000
        track.minutes = int(duree // 60)
        track.secondes = int(duree % 60)

    return render(request, 'disks/detailsAlbum.html', locals())


def recherche(request):
    form = RechercheForm(request.POST)

    if form.is_valid():
        search = form.cleaned_data['search']
        albums = Album.objects.filter(Title__contains=search)
        artists = Artist.objects.filter(Name__contains=search)
        tracks = Track.objects.filter(Name__contains=search)
        return render(request, 'disks/recherche.html', locals())
    return render(request, 'disks/tousAlbums.html')

