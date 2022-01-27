from rest_framework import serializers

# App specific imports
from allNotes.models import NoteModel


class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NoteModel
        # fields = "__all__"
        exclude = ('id',)