from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_about = models.CharField(max_length=200)
    movie_released = models.BooleanField(default=True)

    def __str__(self):
        return self.movie_name

    class Meta:
        verbose_name = "Movie List"
        verbose_name_plural = "Movies List"