from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)

from ..models import Author
from ..serializers import AuthorSerializer, AuthorBooksListSerializer


class AuthorListCreateView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorBooksListAPIView(ListAPIView):
    serializer_class = AuthorBooksListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Author.objects.filter(pk=pk)

        return queryset
