from django.contrib.auth.models import User
from django.db.models.query_utils import Q
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

@api_view(['POST'])
def search_bookreviews(request):
    """POST 방식으로 독후감 검색"""
    search_query = request.data.get('search', '')

    queryset = BookReview.objects.filter(is_deleted=False).filter(
        Q(title__icontains=search_query) |
        Q(book_title__icontains=search_query) |
        Q(book_author__icontains=search_query)
    )
    return Response({
        'status' : 'success',
        'data' : BookReviewListSerializer(queryset, many=True).data
    })

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

    def get_queryset(self):
        """검색 기능 추가"""
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(book_title__icontains=search) |
                Q(book_author__icontains=search)
            )

        return queryset