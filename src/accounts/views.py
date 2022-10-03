from django.shortcuts import render  # NOQA

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import RegistrationForm, UserTypeForm


class IndexView(TemplateView):
    template_name = "index/index.html"


class UserTypeChoice(CreateView):
    form_class = UserTypeForm
    template_name = "registration/user_type_choice.html"
    success_url = reverse_lazy("accounts:registration")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False

        return super().form_valid(form)


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = "registration/user_form.html"
    success_url = reverse_lazy("config:core")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()

        return super().form_valid(form)
