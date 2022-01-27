from django.urls import path

# App specific imports 
from .views import notes_cud, notes_view


urlpatterns = [
    path('notes/', notes_view.as_view(), name='notes-fetch'),
    path('notes/<slug:slug>', notes_cud.as_view(), name='notes-detail')
]