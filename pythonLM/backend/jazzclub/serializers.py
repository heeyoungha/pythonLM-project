from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Artist, Song, SongReview


class ArtistSerializer(serializers.ModelSerializer):
    """아티스트 Serializer"""
    class Meta:
        model = Artist
        fields = ["id", "name"]


class SongSerializer(serializers.ModelSerializer):
    """곡 Serializer (역할별 아티스트 정보 포함)"""
    vocalists = ArtistSerializer(source='get_vocalists', many=True, read_only=True)
    composers = ArtistSerializer(source='get_composers', many=True, read_only=True)
    lyricists = ArtistSerializer(source='get_lyricists', many=True, read_only=True)
    performers = ArtistSerializer(source='get_performers', many=True, read_only=True)

    class Meta:
        model = Song
        fields = ["id", "title", "album", "bpm", "vocalists", "composers", "lyricists", "performers", "created_at",
                  "updated_at"]

class SongReviewSerializer(serializers.ModelSerializer):
    # 읽기 전용 필드들 (자동으로 채워짐)
    song = SongSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    # 입력 필드들
    song_id = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.filter(deleted_at__isnull=True),
        source="song",
        write_only=True
    )

    # 아티스트 ID들 (역할별)
    vocalist_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        allow_empty=True,
        write_only=True
    )
    composer_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        allow_empty=True,
        write_only=True
    )
    lyricist_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        allow_empty=True,
        write_only=True
    )
    performer_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        allow_empty=True,
        write_only=True
    )

    class Meta:
        model = SongReview
        fields = [
            "id", "song", "song_id", "user",
            "vocalist_ids", "composer_ids", "lyricist_ids", "performer_ids",
            'reason_choice', 'one_line_review', 'recommendation_theme', 'feeling', 'url', 'review_text',
            'achievement', 'significance', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        """SongReview 생성 시 Song의 아티스트 정보도 함께 업데이트"""
        # 아티스트 ID들 추출
        vocalist_ids = validated_data.pop('vocalist_ids', [])
        composer_ids = validated_data.pop('composer_ids', [])
        lyricist_ids = validated_data.pop('lyricist_ids', [])
        performer_ids = validated_data.pop('performer_ids', [])

        # Song의 아티스트 정보 업데이트
        song = validated_data['song']
        song.vocalists = vocalist_ids
        song.composers = composer_ids
        song.lyricists = lyricist_ids
        song.performers = performer_ids
        song.save()

        # SongReview 생성
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """SongReview 업데이트 시 Song의 아티스트 정보도 함께 업데이트"""
        # 아티스트 ID들 추출
        vocalist_ids = validated_data.pop('vocalist_ids', None)
        composer_ids = validated_data.pop('composer_ids', None)
        lyricist_ids = validated_data.pop('lyricist_ids', None)
        performer_ids = validated_data.pop('performer_ids', None)

        # Song의 아티스트 정보 업데이트 (값이 제공된 경우에만)
        song = instance.song
        if vocalist_ids is not None:
            song.vocalists = vocalist_ids
        if composer_ids is not None:
            song.composers = composer_ids
        if lyricist_ids is not None:
            song.lyricists = lyricist_ids
        if performer_ids is not None:
            song.performers = performer_ids
        song.save()

        # SongReview 업데이트
        return super().update(instance, validated_data)


# 아티스트 검색을 위한 시리얼라이저
class ArtistSearchSerializer(serializers.ModelSerializer):
    """아티스트와 관련된 곡 3개를 포함한 검색용 시리얼라이저"""
    related_songs = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ["id", "name", "related_songs"]

    def get_related_songs(self, obj):
        """해당 아티스트와 관련된 곡 3개 반환"""
        # 아티스트가 참여한 곡들을 찾기
        songs = Song.objects.filter(
            Q(vocalists__contains=[obj.id]) |
            Q(composers__contains=[obj.id]) |
            Q(lyricists__contains=[obj.id]) |
            Q(performers__contains=[obj.id]),
            deleted_at__isnull=True
        )[:3]

        result = []
        for song in songs:
            # 해당 아티스트의 역할 찾기
            roles = []
            if obj.id in song.vocalists:
                roles.append("vocal")
            if obj.id in song.composers:
                roles.append("composer")
            if obj.id in song.lyricists:
                roles.append("lyricist")
            if obj.id in song.performers:
                roles.append("performer")

            result.append({
                'id': song.id,
                'title': song.title,
                'album': song.album,
                'roles': roles
            })

        return result