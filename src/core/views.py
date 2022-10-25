from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Sum
from django.shortcuts import render  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import CustomAuthenticationForm, RegistrationForm
from volunteering.models import Need


class IndexView(TemplateView):
    template_name = "index/index.html"
    extra_context = {
        "money_donated": float((Need.objects.aggregate(Sum('price'))).get('price__sum')),
        "number_of_requests": Need.objects.filter(is_satisfied=True).count()
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


class Login(LoginView):
    authentication_form = CustomAuthenticationForm


class Logout(LogoutView):
    pass
