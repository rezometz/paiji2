from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Message, MessageIcon
from django.forms import ModelForm, RadioSelect, ModelChoiceField

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
    paginate_by = 10
    queryset = Message.objects.filter(question=None).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context['object_list'] = _with_padding(_depth_browse(context['object_list']))
        return context


class NewMessagesView(ListView):

    template_name = 'forum/new_messages.html'
    paginate_by = 20
    queryset = Message.objects.order_by('-pub_date')


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


def message_view(request, pk):
    context = _get_message_context(pk)
    message = context['message']
    if request.user != message.author:
        message.lectures += 1
        message.save()
    return render(request, 'forum/message_detail.html', context)

def topic_view(request, pk):
    context = _get_message_context(pk)
    return render(request, 'forum/topic.html', context)

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
        return context

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
        
