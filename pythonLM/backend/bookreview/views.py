from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import BookReview
from .serializers import BookReviewListSerializer, BookReviewSerializer


# Create your views here.
@api_view(['GET'])
def hello_rest_api(request):
    data = {'message': 'Hello, Rest API!'}
    return Response(data)

class BookReviewViewSet(viewsets.ModelViewSet):
    """독후감 게시판 CRUD """

    queryset = BookReview.objects.filter(is_deleted=False)
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """Serializer 선택"""
        if self.action == 'list':
            return BookReviewListSerializer
        return BookReviewSerializer

    def perform_create(self, serializer):
        """작성자 정보 추가"""
        if self.request.user.is_authenticated:
            serializer.save(reader=self.request.user)
        else:
            default_user = User.objects.first()
            if not default_user:
                default_user = User.objects.create_user('anonymous', 'example.test.com', 'password')
            serializer.save(reader=default_user)

    
    def perform_destroy(self, instance):
        """소프트 삭제 구현"""
        instance.is_deleted = True
        instance.save()