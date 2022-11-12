from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from volunteering.models import Need, Opportunity, Accounting
from volunteering.tasks import (
    generate_category,
    generate_user,
    generate_opportunity,
    generate_accounting,
    generate_need,
)


# TODO category as in stackoverflow


class AllNeeds(TemplateView):
    model = Need
    template_name = "volunteering/need_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    extra_context = {"needs": Need.objects.all()}


class CreateNeed(LoginRequiredMixin, CreateView):
    model = Need
    success_url = reverse_lazy("volunteering:needs")
    fields = ["title", "description", "price", "donation", "photo", "category", "city"]

    def form_valid(self, form):
        self.object = form.save(commit=True)
        self.object.author.set([self.request.user])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AllOpportunities(TemplateView):
    model = Opportunity
    template_name = "volunteering/opportunity_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    extra_context = {"opportunities": Opportunity.objects.all()}


class CreateOpportunity(CreateView):
    model = Opportunity
    success_url = reverse_lazy("volunteering:opportunities")
    fields = ["title", "description", "photo", "category", "city"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AllAccounting(TemplateView):
    model = Accounting
    template_name = "volunteering/accounting_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    extra_context = {"accounting": Accounting.objects.all()}


class CreateAccounting(CreateView):
    model = Accounting
    success_url = reverse_lazy("volunteering:accounting")
    fields = "__all__"


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
