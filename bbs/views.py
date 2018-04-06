from django.views.generic import ListView, DetailView

from .models import Thread


class ThreadList(ListView):
    model = Thread


class ThreadDetail(DetailView):
    model = Thread

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response_list'] = context['thread'].response_set.all()
        return context
