from django.http import HttpResponse
from django.shortcuts import render  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from volunteering.models import Need
from volunteering.tasks import generate_category, generate_user, generate_opportunity, generate_accounting, \
    generate_need


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


def user_generator(request):
    generate_user.delay()
    return HttpResponse("User created!")


def category_generator(request):
    generate_category.delay()
    return HttpResponse("Category created!")


def accounting_generator(request):
    generate_accounting.delay()
    return HttpResponse("Accounting created!")


def need_generator(request):
    generate_need.delay()
    return HttpResponse("Need created!")


def opportunity_generator(request):
    generate_opportunity.delay()
    return HttpResponse("Opportunity created!")
