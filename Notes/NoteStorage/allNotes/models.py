from django.db import models
from django.utils.text import slugify
from django.urls.base import reverse

# Create your models here.

class NoteModel(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    # slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def __str__(self) -> str:
        return "{}".format(self.title)
    
    # def get_absolute_url(self):
    #     return reverse("notes_detail", args=[self.slug])

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'