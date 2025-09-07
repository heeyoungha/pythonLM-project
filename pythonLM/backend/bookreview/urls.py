from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookReviewViewSet, search_bookreviews

router = DefaultRouter()
router.register(r'', BookReviewViewSet, basename= 'bookreview')

urlpatterns = [
    path('search/', search_bookreviews, name='search_bookreviews'),
] + router.urls