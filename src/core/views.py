from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render  # NOQA
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import CustomAuthenticationForm, RegistrationForm


class IndexView(TemplateView):
    template_name = "index/index.html"


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = "registration/user_form.html"
    success_url = reverse_lazy("core:core")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = True
        self.object.save()

        return super().form_valid(form)


class Login(LoginView):
    authentication_form = CustomAuthenticationForm


class Logout(LogoutView):
    pass
