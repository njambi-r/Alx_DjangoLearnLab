# Permissions and Groups in bookshelf

## Permissions Defined:
- `can_view`: Can view book.
- `can_create`: Can create book.
- `can_edit`: Can edit book.
- `can_delete`: Can delete book.

## Groups:
- **Viewers**: Only `can_view`
- **Editors**: `can_view`, `can_edit`, `can_create`
- **Admins**: Full access

## How to Use:
1. Assign users to groups via Django Admin.
2. Permissions are enforced in views using `@permission_required`.
3. Test by logging in with different user roles.
