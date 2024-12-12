from django.urls import path
from . import views

urlpatterns = [
    # Post CRUD URLs
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Comment CRUD URLs
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),  # Corrected for creating comments
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='update_comment'),  # Corrected for updating comments
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),  # Corrected for deleting comments
]

from django.urls import path
from . import views

urlpatterns = [
    # Other URLs...

    # Search URL
    path('search/', views.search, name='search'),

    # Tag-based filtering
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post_by_tag'),
]
