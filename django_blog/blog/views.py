from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy

# Create View for Comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})

# Update View for Comment
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def get_queryset(self):
        # Ensure users can only edit their own comments
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})

# Delete View for Comment
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_queryset(self):
        # Ensure users can only delete their own comments
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})
