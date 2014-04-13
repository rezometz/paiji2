from django.views import generic

from .models import Note


class NoteListView(generic.ListView):
    model = Note
    paginate_by = 10
    context_object_name = 'notes'

    def get_queryset(self):
        return super(NoteListView, self).get_queryset().select_related(
            'author'
        )

