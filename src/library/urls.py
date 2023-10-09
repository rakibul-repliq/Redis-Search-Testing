from django.urls import path

from library.views import BookSearchView

urlpatterns = [
    path("", BookSearchView.as_view(), name="book-search"),

]