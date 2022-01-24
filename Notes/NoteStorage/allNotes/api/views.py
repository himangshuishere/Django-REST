# Module specific imports
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import *
from rest_framework.views import *
from rest_framework.response import Response

# App specific imports
from allNotes.api.serializers import NoteSerializer
from allNotes.models import NoteStorage

# Class for displaying all the notes...
class notes_fetch(ListCreateAPIView):
    queryset = NoteStorage.objects.all()
    serializer_class = NoteSerializer
    # def get(self):
    #     mainModel = NoteStorage.objects.all()
    #     mainSerializer = NoteSerializer(mainModel, many=True)
        

# Class for creating a note...
class notes_create(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = NoteStorage.objects.all()
    lookup_fields = ['pk',]
    
    # def get(self, request):
    #     dbData = NoteStorage.objects.all()
    #     serializer = NoteSerializer(dbData)
    #     return Response(serializer.data)
        
