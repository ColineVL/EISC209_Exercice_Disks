from django.contrib import admin
from django.contrib import admin
from .models import Album, Artist, Track

# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Track)


class ArtistAdmin(admin.ModelAdmin):
    list_display = 'name'
    list_filter = 'name'
    search_fields = 'name'


class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'composer', 'milliseconds', 'UnitPrice')
    list_filter = ('name', 'album',)
    search_fields = ('name', 'album', 'composer')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artiste')
    list_filter = ('title', 'artiste')
    search_fields = ('title', 'artiste')
