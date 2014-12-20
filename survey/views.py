from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .forms import SurveyVoteForm
from .models import Vote, Poll


class SurveyVoteView(generic.CreateView):
    model = Vote
    form_class = SurveyVoteForm

    def get_form_kwargs(self):
        kwargs = super(SurveyVoteView, self).get_form_kwargs()
        self.poll = Poll.objects.current()
        kwargs['poll'] = self.poll
        return kwargs

    def form_valid(self, form):
        poll = form.save(commit=False)
        poll.user = self.request.user
        return super(SurveyVoteView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request,  _(
            "Your vote has been successfully saved."
        ))
        return reverse('index')


class SurveyListView(generic.ListView):
    model = Poll
    paginate_by = 10
    context_object_name = 'polls'
