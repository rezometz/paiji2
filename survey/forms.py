from django import forms

from .models import Poll, Vote


class SurveyVoteForm(forms.ModelForm):
    def __init__(self, poll=None, *args, **kwargs):
        super(SurveyVoteForm, self).__init__(*args, **kwargs)
        poll = poll if poll != None else Poll.objects.current()
        self.fields['choice'].queryset = poll.choices
        self.fields['choice'].empty_label = None
    
    class Meta:
        model = Vote
        fields = ('choice', )
        widgets = {
            'choice': forms.RadioSelect(),
        }
