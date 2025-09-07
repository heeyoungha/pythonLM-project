from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    SongReviewViewSet, ArtistViewSet, SongViewSet,
    search_artists, create_artist
)

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='songs')
router.register(r'artists', ArtistViewSet, basename='artists')
router.register(r'song-reviews', SongReviewViewSet, basename='song-reviews')

urlpatterns = [
    path('search-artists/', search_artists, name='search-artists'),
    path('create-artist/', create_artist, name='create-artist'),
] + router.urls