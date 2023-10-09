from django.core.cache import cache
from django.db.models import Q

from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class BookSearchView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        query = self.request.query_params.get("q", "")

        # Checking the results are already cached in Redis or not.
        results = cache.get(query)

        if not results:
            # querying the database
            query_filter = Q(title__icontains=query) | Q(author__icontains=query)
            results = Book.objects.filter(query_filter)

            serialized_results = self.serializer_class(results, many=True).data

            # Cache the serialized search results in Redis for future use
            cache.set(query, serialized_results)

        return results
