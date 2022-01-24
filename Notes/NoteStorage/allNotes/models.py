from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NoteStorage(models.Model):
    noteTitle = models.CharField(max_length=20)
    noteContent = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorName')

    def __str__(self) -> str:
        return '{} {}'.format(self.noteTitle, self.author)

    class Meta:
        verbose_name = "Note Storage"
        verbose_name_plural = 'Notes Storage'