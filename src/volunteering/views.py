from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView

from volunteering.models import Need, Opportunity, Accounting, Category
from volunteering.tasks import (
    generate_category,
    generate_user,
    generate_opportunity,
    generate_accounting,
    generate_need,
)


class RedirectToPreviousMixin:
    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']


# TODO category as in stackoverflow


class NeedView(TemplateView):
    model = Need
    template_name = "volunteering/need.html"

    def get(self, request, *args, **kwargs):
        self.extra_context = {"need": Need.objects.get(id=kwargs["pk"])}

        return self.render_to_response(self.extra_context)


class AllNeeds(TemplateView):
    model = Need
    template_name = "volunteering/need_list.html"

    def get(self, request, *args, **kwargs):
        needs = Need.objects.all()
        self.extra_context = {"needs": needs}

        return self.render_to_response(self.extra_context)


class CreateNeed(LoginRequiredMixin, CreateView):
    model = Need
    success_url = reverse_lazy("volunteering:needs")
    fields = ["title", "description", "price", "donation", "category", "city"]

    extra_context = {"categories": Category.objects.all()}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateNeed(RedirectToPreviousMixin, LoginRequiredMixin, UpdateView):
    model = Need
    fields = ["title", "description", "price", "donation", "category", "city"]


class DeleteNeed(RedirectToPreviousMixin, LoginRequiredMixin, DeleteView):
    model = Need

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class OpportunityView(TemplateView):
    model = Opportunity
    template_name = "volunteering/opportunity.html"

    def get(self, request, *args, **kwargs):
        self.extra_context = {"opportunity": Opportunity.objects.get(id=kwargs["pk"])}

        return self.render_to_response(self.extra_context)


class AllOpportunities(TemplateView):
    model = Opportunity
    template_name = "volunteering/opportunity_list.html"

    def get(self, request, *args, **kwargs):
        opportunities = Opportunity.objects.all()
        self.extra_context = {"opportunities": opportunities}

        return self.render_to_response(self.extra_context)


class CreateOpportunity(CreateView):
    model = Opportunity
    success_url = reverse_lazy("volunteering:opportunities")
    fields = ["title", "description", "category", "city"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateOpportunity(RedirectToPreviousMixin, LoginRequiredMixin, UpdateView):
    model = Opportunity
    fields = ["title", "description", "category", "city"]


class DeleteOpportunity(RedirectToPreviousMixin, LoginRequiredMixin, DeleteView):
    model = Opportunity

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class AccountingView(TemplateView):
    model = Accounting
    template_name = "volunteering/accounting.html"

    def get(self, request, *args, **kwargs):
        self.extra_context = {"account": Accounting.objects.get(id=kwargs["pk"])}

        return self.render_to_response(self.extra_context)


class AllAccounting(TemplateView):
    model = Accounting
    template_name = "volunteering/accounting_list.html"

    def get(self, request, *args, **kwargs):
        accounting = Accounting.objects.all()
        self.extra_context = {"accounting": accounting}

        return self.render_to_response(self.extra_context)


class CreateAccounting(CreateView):
    model = Accounting
    success_url = reverse_lazy("volunteering:accounting")
    fields = ["description"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateAccounting(RedirectToPreviousMixin, LoginRequiredMixin, UpdateView):
    model = Accounting
    fields = ["description"]


class DeleteAccounting(RedirectToPreviousMixin, LoginRequiredMixin, DeleteView):
    model = Accounting

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


@user_passes_test(lambda user: user.is_superuser)
def user_generator(request):
    generate_user.delay()
    return HttpResponse("User created!")


@user_passes_test(lambda user: user.is_superuser)
def category_generator(request):
    generate_category.delay()
    return HttpResponse("Category created!")


@user_passes_test(lambda user: user.is_superuser)
def accounting_generator(request):
    generate_accounting.delay()
    return HttpResponse("Accounting created!")


@user_passes_test(lambda user: user.is_superuser)
def need_generator(request):
    generate_need.delay()
    return HttpResponse("Need created!")


@user_passes_test(lambda user: user.is_superuser)
def opportunity_generator(request):
    generate_opportunity.delay()
    return HttpResponse("Opportunity created!")
