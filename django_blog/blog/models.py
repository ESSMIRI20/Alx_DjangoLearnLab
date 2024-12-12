from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)  # Many-to-many relationship with Tag
    # Other fields...

    def __str__(self):
        return self.title

from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = TaggableManager()  # Use TaggableManager to handle tags
    # Other fields...

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Post  # Assuming Post model is in the same app

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model (author of the comment)
    content = models.TextField()  # Content of the comment
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set to current time
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set to current time when updated

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

