from django.contrib import admin

from comics.core import models

class ComicAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'slug', 'url', 'rights')
    prepopulated_fields = {
        'slug': ('name',)
    }

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('comic', 'pub_date')
    list_filter = ['comic', 'pub_date']
    date_hierarchy = 'pub_date'

class ImageAdmin(admin.ModelAdmin):
    list_display = ('comic', 'title', 'fetched')
    list_filter = ['comic', 'fetched']

    date_hierarchy = 'fetched'

admin.site.register(models.Comic, ComicAdmin)
admin.site.register(models.Release, ReleaseAdmin)
admin.site.register(models.Image, ImageAdmin)
