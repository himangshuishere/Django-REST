from django.urls import path

from allNotes.api.views import note_fetch, note_rud

urlpatterns = [
    path('notes/', note_fetch.as_view(), name='all-note'),
    path('notes/<slug:slug>/', note_rud.as_view(), name='note-rud'),
]
