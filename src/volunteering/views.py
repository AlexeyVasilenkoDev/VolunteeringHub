from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView

from volunteering.models import Need, Opportunity, Accounting, Category
from volunteering.tasks import (
    generate_category,
    generate_user,
    generate_opportunity,
    generate_accounting,
    generate_need,
)


class RedirectToPreviousMixin:
    default_redirect = "/"

    def get(self, request, *args, **kwargs):
        request.session["previous_page"] = request.META.get("HTTP_REFERER", self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session["previous_page"]


# TODO category as in stackoverflow


class NeedView(TemplateView):
    model = Need
    template_name = "volunteering/need.html"

    def get(self, request, *args, **kwargs):
        self.extra_context = {"need": Need.objects.get(id=kwargs["pk"])}

        return self.render_to_response(self.extra_context)


class AllNeeds(ListView):
    model = Need
    context_object_name = "needs"
    paginate_by = 10
    ordering = ["date_created"]


class CreateNeed(LoginRequiredMixin, CreateView):
    model = Need
    success_url = reverse_lazy("volunteering:needs")
    fields = ["photo", "title", "description", "price", "donation", "category", "city"]

    extra_context = {"categories": Category.objects.all()}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateNeed(RedirectToPreviousMixin, LoginRequiredMixin, UpdateView):
    model = Need
    fields = ["photo", "title", "description", "price", "donation", "category", "city"]

    def get_object(self):
        object = Need.objects.get(pk=self.kwargs["pk"])
        if self.request.user == object.author:
            return object
        else:
            raise Http404


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


class AllOpportunities(ListView):
    model = Opportunity
    context_object_name = "opportunities"
    paginate_by = 10
    ordering = ["date_created"]


class CreateOpportunity(CreateView):
    model = Opportunity
    success_url = reverse_lazy("volunteering:opportunities")
    fields = ["photo", "title", "description", "category", "city"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateOpportunity(RedirectToPreviousMixin, LoginRequiredMixin, UpdateView):
    model = Opportunity
    fields = ["photo", "title", "description", "category", "city"]

    def get_object(self):
        object = Opportunity.objects.get(pk=self.kwargs["pk"])
        if self.request.user == object.author:
            return object
        else:
            raise Http404


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


class AllAccounting(ListView):
    model = Accounting
    paginate_by = 10
    context_object_name = "accounting"
    ordering = ["date_created"]


class CreateAccounting(CreateView):
    model = Accounting
    success_url = reverse_lazy("volunteering:accounting")
    fields = ["photo", "description"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateAccounting(RedirectToPreviousMixin, LoginRequiredMixin, UpdateView):
    model = Accounting
    fields = ["photo", "description"]

    def get_object(self):
        object = Accounting.objects.get(pk=self.kwargs["pk"])
        if self.request.user == object.author:
            return object
        else:
            raise Http404


class DeleteAccounting(RedirectToPreviousMixin, LoginRequiredMixin, DeleteView):
    model = Accounting

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CategoryView(TemplateView):
    model = Category
    template_name = "volunteering/category.html"

    def get(self, request, *args, **kwargs):
        print(kwargs)
        category = Category.objects.get(name=kwargs["name"].capitalize())
        needs = Need.objects.filter(category__name=kwargs["name"].capitalize())
        opportunities = Opportunity.objects.filter(category__name=kwargs["name"].capitalize())
        accounting = Accounting.objects.filter(needs__category__name=kwargs["name"].capitalize())
        self.extra_context = {
            "category": category,
            "needs": needs,
            "opportunities": opportunities,
            "accounting": accounting,
        }

        return self.render_to_response(self.extra_context)


class AllCategories(ListView):
    model = Category
    template_name = "volunteering/categories_list.html"
    paginate_by = 10
    context_object_name = "categories"

    def get_context_data(self, *, object_list=None, **kwargs):
        category_needs_count = (
            Category.objects.all().annotate(tag=F("name"), count_needs=Count("needs")).values("tag", "count_needs")
        )

        category_opportunities_count = (
            Category.objects.all()
            .annotate(tag=F("name"), count_opportunities=Count("opportunities"))
            .values("tag", "count_opportunities")
        )

        context = {
            "category_needs_count": category_needs_count,
            "category_opportunities_count": category_opportunities_count,
        }

        return super().get_context_data(**context)


class CategoryNeeds(ListView):
    model = Need
    template_name = "volunteering/category_needs.html"
    paginate_by = 10
    context_object_name = "needs"

    def get_queryset(self):
        return Need.objects.filter(category__name=self.kwargs["name"].capitalize())

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        category = Category.objects.get(name=kwargs["name"].capitalize())

        context = self.get_context_data()
        context["category"] = category

        return self.render_to_response(context)


class CategoryOpportunities(ListView):
    model = Category
    template_name = "volunteering/category_opportunities.html"
    paginate_by = 10
    context_object_name = "opportunities"

    def get_queryset(self):
        return Opportunity.objects.filter(category__name=self.kwargs["name"])

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        category = Category.objects.get(name=kwargs["name"].capitalize())

        context = self.get_context_data()
        context["category"] = category

        return self.render_to_response(context)


class HintNeed(TemplateView):
    model = Need
    template_name = "volunteering/hint_need.html"

    def get(self, request, *args, **kwargs):
        current_need = Need.objects.get(pk=kwargs["pk"])
        compare = Need.objects.filter(
            category__opportunities=Opportunity.objects.filter(category__in=current_need.category.all())
        )
        print(compare)


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
