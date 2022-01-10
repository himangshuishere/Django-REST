# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         "movies": list(movies.values())
#     }

#     return JsonResponse(data)


# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         "name": movie.movie_name,
#         "description":movie.movie_about,
#         "active":movie.movie_released
#     }

#     return JsonResponse(data)