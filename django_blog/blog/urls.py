from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
