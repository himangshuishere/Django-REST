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

    def get(self, request, pk):
        try:
            notesFetch = NoteModel.objects.get(pk=pk)
        except NoteModel.DoesNotExist:
            return Response({'Error':'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(notesFetch)
        return Response(serializer.data)
    
    def put(self, request, pk):
        notePut = NoteModel.objects.get(pk=pk)
        serializer = NoteSerializer(notePut, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        noteDelete = NoteModel.objects.get(pk=pk)
        return Response(status=status.HTTP_200_OK)