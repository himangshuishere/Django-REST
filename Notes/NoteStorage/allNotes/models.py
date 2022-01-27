from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NoteModel(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default="", blank=True, null=False)

    def __str__(self):
        return '{} {}'.format(self.title, self.slug)
    
    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'