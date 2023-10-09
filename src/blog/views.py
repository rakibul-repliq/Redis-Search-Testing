from rest_framework import generics

from .models import Post
from .serializers import PostListSerializer
from .search import search_posts


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter()
    serializer_class = PostListSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter()
    serializer_class = PostListSerializer


class SearchPostsView(generics.ListAPIView):
    serializer_class = PostListSerializer
    # queryset = Post.objects.all()

    def get_queryset(self):
        query = self.request.query_params.get("q", "")
        if query:
            return search_posts(query)
        else:
            return Post.objects.none()
