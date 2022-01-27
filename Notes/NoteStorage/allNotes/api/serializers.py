from rest_framework import serializers
from allNotes.models import NoteModel


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NoteModel
        fields = "__all__"
        # fields = ['title', 'content', 'author', 'slug']