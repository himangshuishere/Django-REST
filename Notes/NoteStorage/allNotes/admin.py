from django.contrib import admin
from .models import NoteModel

# Register your models here.

class NoteModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'slug')


admin.site.register(NoteModel, NoteModelAdmin)
