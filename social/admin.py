from django.contrib import admin

from social.models import *
# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'createdOn', 'deletedOn', 'logo', 'newsfeed')

class BureauAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'createdDate', 'endDate')
    ordering = ('-createdDate', )

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'group', 'title', 'public', 'pubDate', 'importance')
    ordering = ('-pubDate', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'author', 'pubDate', 'content')
    ordering = ('message', '-pubDate', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'bureau', 'utilisateur', 'postType')
    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['bureau'].queryset = form.base_fields['bureau'].queryset.filter(endDate = None)
        return form

admin.site.register(PostType)
admin.site.register(GroupCategory)
admin.site.register(Group, GroupAdmin)
admin.site.register(Bureau, BureauAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)
