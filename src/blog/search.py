import redis
from django.conf import settings
from .models import Post  # Import your Post model

# Create a Redis connection
redis_connection = redis.StrictRedis(
    host=settings.CACHES["default"]["LOCATION"], decode_responses=True
)

def search_posts(query):
    """Search for posts containing the query term in the title."""

    query = query.lower()
    post_ids = redis_connection.smembers(f"{query}")
    return Post.objects.filter(pk__in=post_ids)
