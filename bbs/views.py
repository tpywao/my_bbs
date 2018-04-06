from django.views.generic import ListView, DetailView, CreateView

from .models import Thread, Response


class ThreadList(ListView):
    model = Thread


class ThreadDetail(DetailView):
    model = Thread

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response_list'] = context['thread'].response_set.all()
        return context


class ThreadCreate(CreateView):
    model = Thread
    fields = '__all__'
    success_url = '/bbs'


class ResponseCreate(CreateView):
    model = Response
    fields = ('contributor_name', 'content')

    def get_success_url(self):
        return '/bbs/{}'.format(self.kwargs['thread_id'])

    def form_valid(self, form):
        form.instance.thread = Thread.objects.get(pk=self.kwargs['thread_id'])
        return super().form_valid(form)
