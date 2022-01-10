from django.contrib import admin
from .models import *

# Register your models here.

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("title", "storyline")

admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(StreamPlatform)