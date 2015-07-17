from django.contrib import admin

from .models import Message, MessageIcon

class AnswersInline(admin.TabularInline):
    model = Message
    extra = 0

class MessageAdmin(admin.ModelAdmin):
    inlines = [AnswersInline]
    list_display = ('title', 'icon', 'author',\
                    'pub_date',\
                    'is_topic', 'topic', 'level',\
                    'question', 'is_leaf',\
                    'answers_nb', 'childs_nb',\
                    'childs_depth', 'text')
    list_filter = ['pub_date', 'author']
    search_fields = ['title', 'text', 'author']

class MessageIconAdmin(admin.ModelAdmin):
    list_display = ('name', 'filename', 'url')
    search_fields = ['name', 'filename']

admin.site.register(Message, MessageAdmin)
admin.site.register(MessageIcon, MessageIconAdmin)
