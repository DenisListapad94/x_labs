from django.urls import path

from ..views.book_views import (
    BookListCreateView,
    BookDetailView,
)

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
