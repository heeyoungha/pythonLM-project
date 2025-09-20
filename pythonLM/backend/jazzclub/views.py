from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q

from .models import Artist, Song, SongReview
from rest_framework.permissions import AllowAny

from .serializers import ArtistSerializer, SongSerializer, SongReviewSerializer, \
    ArtistSearchSerializer


# Create your views here.

# Create your views here.
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.filter(deleted_at__isnull=True)
    permission_classes = [AllowAny]
    serializer_class = ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.filter(deleted_at__isnull=True)
    permission_classes = [AllowAny]
    serializer_class = SongSerializer


class SongReviewViewSet(viewsets.ModelViewSet):
    queryset = SongReview.objects.filter(deleted_at__isnull=True)
    permission_classes = [AllowAny]
    serializer_class = SongReviewSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            try:
                default_user = User.objects.get(username="anonymous")
            except User.DoesNotExist:
                default_user = User.objects.create_user(username="anonymous", email="example.test.com",
                                                        password="password")
            serializer.save(user=default_user)


# 아티스트 검색 API
@api_view(['GET'])
@permission_classes([AllowAny])
def search_artists(request):
    """아티스트 검색 (관련 곡 3개 포함)"""
    query = request.GET.get('q', '')

    if query:
        artists = Artist.objects.filter(
            Q(name__icontains=query) & Q(deleted_at__isnull=True)
        )[:10]  # 최대 10개 결과
    else:
        artists = Artist.objects.filter(deleted_at__isnull=True)[:20]  # 기본 20개

    serializer = ArtistSearchSerializer(artists, many=True)
    return Response(serializer.data)


# 아티스트 추가 API
@api_view(['POST'])
@permission_classes([AllowAny])
def create_artist(request):
    """새로운 아티스트 추가"""
    name = request.data.get('name', '').strip()

    if not name:
        return Response(
            {'error': '아티스트 이름이 필요합니다.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # 중복 확인
    if Artist.objects.filter(name=name, deleted_at__isnull=True).exists():
        return Response(
            {'error': '이미 존재하는 아티스트입니다.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    artist = Artist.objects.create(name=name)
    serializer = ArtistSearchSerializer(artist)

    return Response(serializer.data, status=status.HTTP_201_CREATED)