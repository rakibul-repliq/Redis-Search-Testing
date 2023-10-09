from django.urls import path

from .views import PostList, PostDetail, SearchPostsView

urlpatterns = [
    path("/posts", PostList.as_view(), name="post-list"),
    path("/posts/<int:pk>", PostDetail.as_view(), name="post-detail"),
    path("/search", SearchPostsView.as_view(), name="search-posts"),
]
