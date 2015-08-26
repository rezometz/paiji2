from django.contrib import admin

from social import models


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'createdOn',
        'deletedOn',
        'logo',
        'newsfeed',
    )


class BureauAdmin(admin.ModelAdmin):
    list_display = (
        'group',
        'createdDate',
        'endDate',
    )
    ordering = ('-createdDate', )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'group',
        'title',
        'public',
        'pubDate',
        'importance',
    )
    ordering = ('-pubDate', )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'author',
        'pubDate',
        'content',
    )
    ordering = ('message', '-pubDate', )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'bureau',
        'utilisateur',
        'postType',
    )


admin.site.register(models.PostType)
admin.site.register(models.GroupCategory)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Bureau, BureauAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Comment, CommentAdmin)
