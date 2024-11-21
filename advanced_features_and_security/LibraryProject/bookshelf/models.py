from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        permissions = [
            ('can_view', 'Can view post'),
            ('can_create', 'Can create post'),
            ('can_edit', 'Can edit post'),
            ('can_delete', 'Can delete post'),
        ]

    def __str__(self):
        return self.title