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
