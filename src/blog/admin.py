from django.contrib import admin

from . models import Post
# Register your models here.


@admin.register(Post)
class Postdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "created_at"]