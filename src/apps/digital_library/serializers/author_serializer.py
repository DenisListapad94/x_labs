from rest_framework import serializers

from .book_serializer import BookSerializer
from ..models.author_model import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("first_name", "last_name", "birth_date")


class AuthorBooksListSerializer(serializers.ModelSerializer):
    author_books = BookSerializer(many=True, source="books")

    class Meta:
        model = Author
        fields = ("first_name", "last_name", "author_books")
