from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, CreateView, TemplateView, RedirectView
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Message, MessageIcon
from django.forms import ModelForm, RadioSelect, ModelChoiceField, TextInput, Textarea

PADDING = 30

def _depth_browse(arg):
    L = []
    for answer in arg:
        L.append(answer)
        if not answer.is_leaf():
            L += _depth_browse(answer.answers.all())
    return L


def _with_padding(L):
    return zip(L, [PADDING * obj.level() for obj in L])


class TopicListView(ListView):

    template_name = 'forum/index.html'
    paginate_by = 15
    queryset = Message.objects.filter(question=None).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context['object_list'] = _with_padding(_depth_browse(context['object_list']))
        context['expand'] = self.request.session.get('expand', True)
        context['button'] = True
        return context


class NewMessagesView(ListView):

    template_name = 'forum/new_messages.html'
    paginate_by = 30
    queryset = Message.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['expand'] = self.request.session.get('expand', True)
        return context


def _get_message_context(pk):
    message = get_object_or_404(Message, pk=pk)

    # previous and next topics
    topic = message.topic()
    try:
        next_topic = Message.objects.filter(question=None).filter(pub_date__gt=topic.pub_date).earliest('pub_date')
    except:
        next_topic = None
    try:
        prev_topic = Message.objects.filter(question=None).filter(pub_date__lt=topic.pub_date).latest('pub_date')
    except:
        prev_topic = None

    # question answered
    question = message.question

    # message list
    L = _depth_browse([topic])
    object_list = _with_padding(L)

    # lower and upper messages
    i = L.index(message)
    try:
        down = L[i+1]
    except:
        down =  None
    try:
        if i - 1 >= 0:
            up = L[i-1]
        else:
            up = None
    except:
        up =  None

    # previous and next message (time sorted)
    TL = sorted(L, key=lambda msg: msg.pub_date)
    j = TL.index(message)
    try:
        next = TL[j + 1]
    except:
        next = None
    try:
        if j - 1 >= 0:
            prev = TL[j - 1]
        else:
            prev = None
    except:
        prev = None

    context = dict(
        object_list=object_list,
        message=message,
        question=question,
        next_topic=next_topic,
        prev_topic=prev_topic,
        next=next,
        prev=prev,
        up=up,
        down=down,
    )
    return context


class MessageView(TemplateView):

    template_name = 'forum/message_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        context = _get_message_context(self.kwargs['pk'])
        context['url_name'] = 'forum:message'
        return context


class TopicView(MessageView):

    template_name = 'forum/topic.html'

    def get_context_data(self, **kwargs):
        context = super(TopicView, self).get_context_data(**kwargs)
        context['url_name'] = 'forum:topic'
        return context


class IconField(ModelChoiceField):

    def label_from_instance(self, obj):
        #return '<img class="icon" src="'+obj.url()+'" alt="'+obj.name+'"/>'
        return obj.url()


class AnswerForm(ModelForm):

    icon = IconField(
        queryset=MessageIcon.objects.all(),
        empty_label=None,
        widget=RadioSelect,
    )

    class Meta:
        model = Message
        fields = ['icon', 'title', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control'}),
        }
            


class AnswerCreate(CreateView):

    form_class = AnswerForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AnswerCreate, self).dispatch(*args, **kwargs)

    def get_template_names(self):
        if 'pk' in self.kwargs:
            return ['forum/answer.html']
        else:
            return ['forum/new.html']

    def get_context_data(self, **kwargs):
        context = super(AnswerCreate, self).get_context_data(**kwargs)
        try:
            # real answer
            context.update(_get_message_context(self.kwargs['pk']))
        except:
            # new topic
            pass
        if self.request.session.get('expand', True):
            context['url_name'] = 'forum:topic'
        else:
            context['url_name'] = 'forum:message'
        return context

    def get_success_url(self):
        if self.request.session.get('expand', True):
            return reverse('forum:topic', args=[self.object.pk]) + "#forum-message"
        else:
            return reverse('forum:message', args=[self.object.pk])+ "#forum-message"

        
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.pub_date = timezone.now()
        form.instance.lectures = 1
        try:
            # real answer
            form.instance.question = Message.objects.get(pk=self.kwargs['pk'])
        except:
            # new topic
            form.instance.question = None
        #form.instance.icon = MessageIcon.objects.all()[0]
        return super(AnswerCreate, self).form_valid(form)
        
class ChangeExpandPref(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        prev = self.request.session.get('expand', True)
        self.request.session['expand'] = not prev
        return reverse('forum:topic-list')

