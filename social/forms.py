from django import forms
from django.utils.translation import ugettext as _

from .models import Comment  # ,Message


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = _('Write a comment...')

    class Meta:
        model = Comment
        fields = ('content', )
