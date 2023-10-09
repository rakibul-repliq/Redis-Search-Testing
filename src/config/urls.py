from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/blog", include('blog.urls')),
    
    path("api/books", include('library.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path("__debug__/", include("debug_toolbar.urls")),
]
