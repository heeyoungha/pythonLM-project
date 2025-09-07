from rest_framework import serializers

from .models import BookReview


class BookReviewSerializer(serializers.ModelSerializer):
    reader_name = serializers.CharField(source="reader.username", read_only=True)
    tag_list = serializers.ReadOnlyField()
    
    """독후감 Serializer"""
    class Meta:
        model = BookReview
        fields = [
            'id', 'title', 'content', 'book_title', 'book_author',
            'rating', 'read_date', 'discussion_topic', 'tags', 'tag_list',
            'reader_name', 'created_at', 'updated_at'
        ]
        read_only_fields = ['reader_name', 'created_at', 'updated_at']

class BookReviewListSerializer(serializers.ModelSerializer):
    """독후감 리스트 Serializer"""

    reader_name = serializers.CharField(source="reader.username", read_only=True)
    tag_list = serializers.ReadOnlyField()

    class Meta:
        model = BookReview
        fields = [
            'id', 'title', 'book_title', 'book_author', 
            'rating', 'read_date', 'tags', 'tag_list',
            'reader_name', 'created_at'
        ]