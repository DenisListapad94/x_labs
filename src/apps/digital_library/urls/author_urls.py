from django.urls import path

from ..views.author_views import (
    AuthorListCreateView,
    AuthorDetailView,
    AuthorBooksListAPIView,
)

urlpatterns = [
    path('', AuthorListCreateView.as_view(), name='author-list-create'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('<int:pk>/books', AuthorBooksListAPIView.as_view(), name='author-books-list'),
]
