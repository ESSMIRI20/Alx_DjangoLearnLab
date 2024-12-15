from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Post, Like
from accounts.models import CustomUser  # Or User, depending on your model name
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    # Get all users that the current user is following
    following_users = request.user.following.all()

    # Get posts from followed users, ordered by creation date (most recent first)
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    # Serialize posts
    post_data = [
        {
            "id": post.id,
            "content": post.content,
            "created_at": post.created_at,
            "author": post.author.username,
        }
        for post in posts
    ]

    return Response(post_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post,
        )
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
    return Response({'status': 'already liked'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    deleted, _ = Like.objects.filter(user=request.user, post=post).delete()
    if deleted:
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
    return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)
