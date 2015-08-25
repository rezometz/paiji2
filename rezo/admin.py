from django.contrib import admin
from django import forms
from modular_blocks.fields import ListTextField

from .models import User

class TextListInput(forms.TextInput):
# widget for the admin editing
# of sidebar_left and sidebar_right
    def _format_value(self, value):
        return ','.join(value)

class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ListTextField: {
            'widget': TextListInput,
        },
    }
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'sidebar_left',
        'sidebar_right',
    )
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
    )


admin.site.register(User, UserAdmin)
