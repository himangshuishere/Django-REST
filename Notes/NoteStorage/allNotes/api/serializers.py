from rest_framework import serializers

from allNotes.models import NoteStorage

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteStorage
        # exclude = ('author',)
        fields = "__all__"