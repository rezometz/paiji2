from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'sidebar_left', 'sidebar_right', )
    search_fields = ('username', 'first_name', 'last_name', 'email', )

admin.site.register(User, UserAdmin)
