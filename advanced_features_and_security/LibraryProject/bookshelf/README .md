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


# Permissions and Group-Based Access Control in Bookshelf App

### Overview

This app uses Django's groups and permissions to control access to the `Book` model. Permissions are set up to restrict viewing, creating, editing, and deleting actions to specific user roles.

### Custom Permissions

The `Book` model has the following custom permissions:
- `can_view`: Allows viewing of books
- `can_create`: Allows creating new books
- `can_edit`: Allows editing books
- `can_delete`: Allows deleting books

### User Groups

Groups with assigned permissions:
- **Viewers**: Can only view books (`can_view`)
- **Editors**: Can view, create, and edit books (`can_view`, `can_create`, `can_edit`)
- **Admins**: Full access to all actions on books (`can_view`, `can_create`, `can_edit`, `can_delete`)

### Enforcing Permissions in Views

Views are protected by decorators that check for specific permissions. If a user lacks permission, access is denied.

For example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    ...
