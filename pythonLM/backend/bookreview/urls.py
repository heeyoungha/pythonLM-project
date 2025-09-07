from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookReviewViewSet

router = DefaultRouter()
router.register(r'', BookReviewViewSet, basename= 'bookreview')

urlpatterns = router.urls

