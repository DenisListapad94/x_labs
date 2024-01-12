from rest_framework import serializers

from ..models.book_model import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "description", "publication_year")
