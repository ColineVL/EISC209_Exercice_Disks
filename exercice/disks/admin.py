from django.contrib import admin
from .models import Album, Artist, Track


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Artist')
    list_filter = ('Title', 'Artist',)
    ordering = ('Title', 'Artist',)
    search_fields = ('Title', 'Artist')


class TrackAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Album', 'Composer', 'Milliseconds', 'UnitPrice')
    list_filter = ('Name', 'Album',)
    search_fields = ('Name', 'Album', 'Composer')


# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist)
admin.site.register(Track, TrackAdmin)
