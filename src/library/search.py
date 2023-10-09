from django.core.cache import cache
from django.db.models import Q

from .models import Book


def search_books(query):
    query_filter = Q(title__icontains=query) | Q(author__icontains=query)
    results = Book.objects.filter(query_filter)
    return results
