from django.views.generic import ListView

from .models import Thread


class ThreadList(ListView):
    model = Thread
