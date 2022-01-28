from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import *
from django.utils.text import slugify
from rest_framework.authtoken.models import Token

# App Specific Import(s)
from allNotes.api.permissions import NoteUser
from allNotes.api.serializers import NoteSerializer
from allNotes.models import NoteModel


class note_fetch(APIView):
    permission_classes = [IsAuthenticated]#, NoteUser]

    def get(self, request):
        # mainToken = Token.objects.get(user=request.user).key
        db = NoteModel.objects.filter(author=request.user)
        serializerClass = NoteSerializer(db, many=True)
        return Response(serializerClass.data)
    
    def post(self, request):
        serializerClass = NoteSerializer(data=request.data)
        if serializerClass.is_valid():
            if 'slug' not in serializerClass.validated_data.keys():
                serializerClass.validated_data['slug'] = slugify(serializerClass.validated_data['title'])
            
            if 'author' not in serializerClass.validated_data.keys():
                # serializerClass.validated_data['author'] = Token.objects.get(key=request.headers['Authorization']).user
                serializerClass.validated_data['author'] = request.user
            serializerClass.save()
            return Response(serializerClass.data)
        
        else: return Response(serializerClass.errors)


class note_rud(APIView): # note_cud => note_RetrieveUpdateDelete
    permission_classes = [NoteUser]
    
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