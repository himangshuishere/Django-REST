from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.movie_list),
    path('list/<int:pk>', views.movie_details)
]
