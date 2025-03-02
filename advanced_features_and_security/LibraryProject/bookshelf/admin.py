from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('title',)
admin.site.register(Book, MemberAdmin)

#customizing user admin interface
class CustomUserAdmin(UserAdmin):
    #define fields to display in the admin panel
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    """
    fieldsets controls which fields appear when viewing/editing a user’s details.
    UserAdmin.fieldsets + (...) keeps Django’s default fields but adds our custom fields
    i.e (date_of_birth, profile_photo).

    In this case, in the Django admin, when you open a user’s profile, you will see a section labeled
    "Additional Info" containing date_of_birth and profile_photo.
    """
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    #add_fieldsets ensures that extra fields appear when creating a new user

#register the custom user model
admin.site.register(CustomUser, CustomUserAdmin)


