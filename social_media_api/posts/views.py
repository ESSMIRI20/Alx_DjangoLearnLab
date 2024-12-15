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

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        # Create a notification
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb="liked your post",
            target=post,
        )
        return JsonResponse({'status': 'liked'})
    return JsonResponse({'status': 'already liked'})

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Like.objects.filter(user=request.user, post=post).delete()
    return JsonResponse({'status': 'unliked'})
