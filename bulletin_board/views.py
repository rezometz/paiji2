from django.views import generic
from django.core.urlresolvers import reverse

from django.utils.translation import ugettext_lazy as _

from django.contrib import messages

from .models import Note


class NoteListView(generic.ListView):
    model = Note
    paginate_by = 10
    context_object_name = 'notes'

    def get_queryset(self):
        return super(NoteListView, self).get_queryset().select_related(
            'author'
        )


class NoteCreateView(generic.CreateView):
    model = Note
    fields = ('message', )

    def form_valid(self, form):
        note = form.save(commit=False)
        note.author = self.request.user
        note.save()

        return super(NoteCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request, _(
            'Your note has been added to the board, '
            'it will be displayed in a moment'
        ))
        success_url = self.request.POST.get('next')
        return success_url if success_url != '' else reverse('index')
