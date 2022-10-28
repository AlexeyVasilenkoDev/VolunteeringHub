from django.shortcuts import render  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from volunteering.models import Need


class AllNeeds(ListView):
    model = Need


class CreateNeed(CreateView):
    model = Need
    success_url = reverse_lazy("core:index")
    fields = "__all__"
