from django.db import models

from .author_model import Author


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

    def __str__(self):
        return self.title
