from django.contrib.auth.models import User
from django.db import models

ROLE_CHOICES = [
        ("vocal", "보컬"),
        ("composer", "작곡"),
        ("lyricist", "작사"),
        ("performer", "연주")
    ]

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Is Deleted")

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    bpm = models.IntegerField(blank=True, null=True)

    # 역할별 아티스트 ID 리스트로 저장
    vocalists = models.JSONField(
        default=list,
        blank=True,
        verbose_name="보컬 아티스트 ID들",
        help_text="[1, 2, 3] 형태의 아티스트 ID 리스트"
    )
    composers = models.JSONField(
        default=list,
        blank=True,
        verbose_name="작곡가 ID들"
    )
    lyricists = models.JSONField(
        default=list,
        blank=True,
        verbose_name="작사가 ID들"
    )
    performers = models.JSONField(
        default=list,
        blank=True,
        verbose_name="연주자 ID들"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Is Deleted")

    def __str__(self):
        return self.title

    def get_vocalists(self):
        """보컬 아티스트 객체들 반환"""
        if not self.vocalists:
            return Artist.objects.none()
        return Artist.objects.filter(id__in=self.vocalists, deleted_at__isnull=True)

    def get_composers(self):
        """작곡가 객체들 반환"""
        if not self.composers:
            return Artist.objects.none()
        return Artist.objects.filter(id__in=self.composers, deleted_at__isnull=True)

    def get_lyricists(self):
        """작사가 객체들 반환"""
        if not self.lyricists:
            return Artist.objects.none()
        return Artist.objects.filter(id__in=self.lyricists, deleted_at__isnull=True)

    def get_performers(self):
        """연주자 객체들 반환"""
        if not self.performers:
            return Artist.objects.none()
        return Artist.objects.filter(id__in=self.performers, deleted_at__isnull=True)

    def get_all_artist_ids(self):
        """모든 참여 아티스트 ID들 반환 (중복 제거)"""
        all_ids = set()
        all_ids.update(self.vocalists)
        all_ids.update(self.composers)
        all_ids.update(self.lyricists)
        all_ids.update(self.performers)
        return list(all_ids)

    def get_all_artists(self):
        """모든 참여 아티스트 객체들 반환"""
        artist_ids = self.get_all_artist_ids()
        if not artist_ids:
            return Artist.objects.none()
        return Artist.objects.filter(id__in=artist_ids, deleted_at__isnull=True)

    def add_vocalist(self, artist_id):
        """보컬 추가"""
        if artist_id not in self.vocalists:
            self.vocalists.append(artist_id)
            self.save()

    def remove_vocalist(self, artist_id):
        """보컬 제거"""
        if artist_id in self.vocalists:
            self.vocalists.remove(artist_id)
            self.save()

class SongReview(models.Model):
    song = models.ForeignKey(Song, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)

    reason_choice = models.CharField(max_length=200, blank=True, null=True, verbose_name="Reason")
    one_line_review = models.TextField(blank=True, null=True, verbose_name="One line review")
    recommendation_theme = models.TextField(blank=True, null=True, verbose_name="Recommendation theme")
    feeling = models.CharField(max_length=200, blank=True, null=True, verbose_name="Feeling")
    url = models.URLField(blank=True, null=True, verbose_name="URL")
    review_text = models.TextField(blank=True, null=True, verbose_name="Review text")

    achievement = models.TextField(blank=True, null=True, verbose_name="Achievement")
    significance = models.TextField(blank=True, null=True, verbose_name="Significance")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Is Deleted")

    class Meta:
        unique_together = ("song", "user")

    def __str__(self):
        return f"{self.song} - {self.user.name}"

    # Song의 역할별 아티스트 객체를 그대로 반환
    @property
    def vocalists(self):
        return self.song.get_vocalists()

    @property
    def composers(self):
        return self.song.get_composers()

    @property
    def lyricists(self):
        return self.song.get_lyricists()

    @property
    def performers(self):
        return self.song.get_performers()

    @property
    def all_artists(self):
        return self.song.get_all_artists()