from datetime import date

from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BookReview(models.Model):

    # 기본 정보
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(verbose_name="Content")

    # 책 정보
    book_title = models.CharField(max_length=200, verbose_name="Book Title")
    book_author = models.CharField(max_length=200, verbose_name="Book Author")
    rating = models.IntegerField(
        choices = [(i,f"{i}점") for i in range(1,6)],
        verbose_name="Rating",
    )

    # 독서 정보
    read_date = models.DateField(default=date.today, verbose_name="Read Date")
    discussion_topic = models.CharField(blank=True, max_length=200, verbose_name="Discussion Topic")
    tags = models.CharField(max_length=500, blank=True, verbose_name="Tags")

    # 메타 정보
    reader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Reader")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    class Meta:
        db_table = "bookreview"
        verbose_name = "Book Review"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} = {self.book_title}"

    @property
    def tag_list(self):
        """태그를 리스트로 반환"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []