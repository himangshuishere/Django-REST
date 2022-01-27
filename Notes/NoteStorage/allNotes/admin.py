from django.contrib import admin

# App specific imports
from .models import NoteModel

# Register your models here.

admin.site.register(NoteModel)