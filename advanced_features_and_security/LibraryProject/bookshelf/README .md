# Permissions and Groups in Django

This Django project uses custom permissions and groups to control access to posts.

## Groups:
- **Admins**: Can view, create, edit, and delete posts.
- **Editors**: Can create and edit posts.
- **Viewers**: Can only view posts.

## Custom Permissions:
- **can_view**: Permission to view posts.
- **can_create**: Permission to create posts.
- **can_edit**: Permission to edit posts.
- **can_delete**: Permission to delete posts.

## Views:
- `post_list`: Only users with `can_view` permission can access.
- `create_post`: Only users with `can_create` permission can access.
- `edit_post`: Only users with `can_edit` permission can access.
- `delete_post`: Only users with `can_delete` permission can access.
