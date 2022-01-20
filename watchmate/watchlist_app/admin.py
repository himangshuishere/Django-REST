from django.contrib import admin
from .models import *

# Register your models here.

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("title", "storyline", "platform")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('watchlist', 'review_user', 'rating', 'description')


admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(StreamPlatform)
admin.site.register(Review, ReviewAdmin)