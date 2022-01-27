from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.generics import *
from rest_framework import status

# App specific imports
from allNotes.models import NoteModel
from .serializers import NoteSerializer


class notes_view(APIView):

    def get(self, request):
        model = NoteModel.objects.all()
        serializer = NoteSerializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else: Response(serializer.errors)


class notes_cud(APIView): # notes_cud => notes_CreateUpdateDelete

    def get(self, request, slug):
        try:
            notesFetch = NoteModel.objects.get(slug=slug)
        except NoteModel.DoesNotExist:
            return Response({'Error':'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(notesFetch)
        return Response(serializer.data)
    
    def put(self, request, slug):
        notePut = NoteModel.objects.get(slug=slug)
        serializer = NoteSerializer(notePut, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, slug):
        noteDelete = NoteModel.objects.get(slug=slug)
        return Response(status=status.HTTP_200_OK)