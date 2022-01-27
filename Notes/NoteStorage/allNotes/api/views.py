from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import *

# App Specific Import(s)
from allNotes.api.serializers import NoteSerializer
from allNotes.models import NoteModel


class note_fetch(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        db = NoteModel.objects.all()
        serializerClass = NoteSerializer(db, many=True)
        return Response(serializerClass.data)
    
    def post(self, request):
        serializerClass = NoteSerializer(data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data)
        
        else: return Response(serializerClass.errors)


class note_rud(APIView): # note_cud => note_RetrieveUpdateDelete
    permission_classes = [IsAuthenticated]
    
    def get(self, request, slug):
        try:
            fetcher = NoteModel.objects.get(slug=slug)
        except NoteModel.DoesNotExist:
            return Response({'Error':'Note not found'}, status = status.HTTP_404_NOT_FOUND)
        serializerClass = NoteSerializer(fetcher)
        return Response(serializerClass.data)

    def put(self, request, slug):
        fetcher = NoteModel.objects.get(slug=slug)
        serializerClass = NoteSerializer(fetcher, data=request.data)
        if serializerClass.is_valid():
            serializerClass.save()
            return Response(serializerClass.data)
        
        else:
            return Response(serializerClass.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        NoteModel.objects.get(slug=slug).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)