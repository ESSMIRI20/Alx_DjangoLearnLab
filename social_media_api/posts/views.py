from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# posts/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from accounts.models import User
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def user_feed(request):
    # Get all users that the current user is following
    following_users = request.user.following.all()
    
    # Get posts from followed users, ordered by creation date (most recent first)
    posts = Post.objects.filter(user__in=following_users).order_by('-created_at')
    
    # Serialize posts
    post_data = []
    for post in posts:
        post_data.append({
            "id": post.id,
            "content": post.content,
            "created_at": post.created_at,
            "user": post.user.username,
        })

    return Response(post_data)
