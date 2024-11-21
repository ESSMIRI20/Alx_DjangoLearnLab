from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Post

class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        post_migrate.connect(create_groups, sender=self)

def create_groups(sender, **kwargs):
    # Create Groups
    admin_group, created = Group.objects.get_or_create(name='Admins')
    editor_group, created = Group.objects.get_or_create(name='Editors')
    viewer_group, created = Group.objects.get_or_create(name='Viewers')

    # Assign Permissions
    can_view = Permission.objects.get(codename='can_view', content_type__app_label='blog')
    can_create = Permission.objects.get(codename='can_create', content_type__app_label='blog')
    can_edit = Permission.objects.get(codename='can_edit', content_type__app_label='blog')
    can_delete = Permission.objects.get(codename='can_delete', content_type__app_label='blog')

    # Admins: can view, create, edit, and delete
    admin_group.permissions.set([can_view, can_create, can_edit, can_delete])

    # Editors: can create and edit
    editor_group.permissions.set([can_create, can_edit])

    # Viewers: can only view
    viewer_group.permissions.set([can_view])
