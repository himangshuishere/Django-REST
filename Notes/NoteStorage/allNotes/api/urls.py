from django.urls import path
from .views import notes_create, notes_fetch

urlpatterns = [
    path('notes/', notes_fetch.as_view(), name="all-notes"),
    path('create-note/<int:pk>', notes_create.as_view(), name='create-note'),
]
