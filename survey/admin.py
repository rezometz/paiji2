from django.contrib import admin

from .models import Poll, Choice, Vote


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]
    list_display = ('title', 'beginning', 'end', )


class VoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)
