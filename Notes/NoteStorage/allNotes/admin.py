from django.contrib import admin

# App specific imports
from .models import NoteModel

# Register your models here.
class NoteModelAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}


admin.site.register(NoteModel, NoteModelAdmin)