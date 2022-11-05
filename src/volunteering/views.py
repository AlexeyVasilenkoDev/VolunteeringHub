from django.shortcuts import render  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from volunteering.models import Need


class AllNeeds(TemplateView):
    model = Need
    template_name = "volunteering/need_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    extra_context = {
        "needs": Need.objects.all()
    }


class CreateNeed(CreateView):
    model = Need
    success_url = reverse_lazy("core:index")
    fields = ["title", "description", "price", "donation", "photo", "category", "city"]
