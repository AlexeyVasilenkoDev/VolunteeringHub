from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import ProgrammingError
from django.db.models import Sum
from django.shortcuts import render  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from psycopg2 import OperationalError

from core.forms import CustomAuthenticationForm, RegistrationForm, ProfileForm
from volunteering.models import Need, Opportunity, Accounting


class IndexView(TemplateView):
    template_name = "index/index.html"
    try:
        extra_context = {
            "money_donated": float((Need.objects.aggregate(Sum('price'))).get('price__sum')) if (
                Need.objects.aggregate(Sum('price'))).get('price__sum') else 0,
            "number_of_requests": Need.objects.filter(is_satisfied=True).count()
        }

    except (OperationalError, ProgrammingError):
        extra_context = {
            "money_donated": 0,
            "number_of_requests": 0
        }


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = "registration/user_form.html"
    success_url = reverse_lazy("core:core")

    def form_valid(self, form):
        self.object = form.save(commit=True)
        self.object.is_active = True
        self.object.save()

        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    model = get_user_model()
    template_name = "accounts/profile.html"

    # extra_context = {
    #     "needs": Need.objects.filter(author=self.)
    # }

    def get(self, request, *args, **kwargs):
        print(kwargs)
        print(kwargs["pk"])
        needs = Need.objects.filter(author=kwargs["pk"])
        opportunities = Opportunity.objects.filter(author=kwargs["pk"])
        accounting = Accounting.objects.filter(author=kwargs["pk"])
        self.extra_context = {"needs": needs,
                              "opportunities": opportunities,
                              "accounting": accounting}

        return self.render_to_response(self.extra_context)


class CreateProfile(CreateView):
    form_class = ProfileForm
    template_name = "accounts/create_profile.html"
    success_url = reverse_lazy("core:core")


class Login(LoginView):
    authentication_form = CustomAuthenticationForm
    next_page = reverse_lazy("core:core")


class Logout(LogoutView):
    next_page = reverse_lazy("core:core")
