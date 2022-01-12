from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status, generics, mixins

from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchlistSerializer, ReviewSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Watchlist.objects.get(pk=pk)
        
        serializer.save(watchlist=movie)


class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, kwargs)


class StreamPlatformVS(viewsets.ViewSet):

    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = generics.get_object_or_404(queryset, many=True)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)

class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        # serializer = StreamPlatformSerializer(platform, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else: return Response(serializer.errors)
    

class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            sp = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Streaming Platform Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(sp)
        return Response(serializer.data)

    def put(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        StreamPlatform.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = WatchlistSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error':'Watchlist Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializers = WatchlistSerializer(movie)
        return Response(serializers.data)


    def put(self, request, pk):
        
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

    def delete(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

           
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Watchlist.objects.all()
#         serializer_for_movie = WatchlistSerializer(movies, many=True)
#         return Response(serializer_for_movie.data)

#     if request.method == 'POST':
#         serializer = WatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

#     if request.method == 'GET':
#         try:
#             movie = Watchlist.objects.get(pk=pk)
#         except Watchlist.DoesNotExist:
#             return Response({'Error':'Watchlist Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serializers = WatchlistSerializer(movie)
#         return Response(serializers.data)
    
#     if request.method == 'PUT':
#         movie = Watchlist.objects.get(pk=pk)
#         serializer = WatchlistSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

#     if request.method == 'DELETE':
#         movie = Watchlist.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.is_client_error())