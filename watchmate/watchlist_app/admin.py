from django.contrib import admin
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ("movie_name", "movie_about")

admin.site.register(Movie, MovieAdmin)