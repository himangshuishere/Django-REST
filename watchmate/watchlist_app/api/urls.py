from django.urls import path, include
from watchlist_app.api.views import ReviewList, ReviewDetail, StreamPlatformAV, StreamPlatformDetailAV, StreamPlatformMVS, UserReview, WatchListAV, WatchDetailAV, ReviewCreate, WatchListGV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream/', StreamPlatformMVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('query/', WatchListGV.as_view(), name='watch-list-query'),
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream'),


    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('review/', UserReview.as_view(), name='user-review-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
