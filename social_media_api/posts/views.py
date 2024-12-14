# posts/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from accounts.models import CustomUser  # Or User, depending on your model name
from rest_framework.permissions import IsAuthenticated  # Import the permission
from rest_framework import status

@api_view(['GET'])
def user_feed(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    # Get all users that the current user is following
    following_users = request.user.following.all()
    
    # Get posts from followed users, ordered by creation date (most recent first)
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    # Serialize posts
    post_data = []
    for post in posts:
        post_data.append({
            "id": post.id,
            "content": post.content,
            "created_at": post.created_at,
            "author": post.author.username,  # Correct field for the user who created the post
        })

    return Response(post_data)
