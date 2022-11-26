from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import ProgrammingError
from django.db.models import Sum, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from psycopg2 import OperationalError

from accounts.models import Profile
from core.forms import CustomAuthenticationForm, RegistrationForm
from volunteering.models import Need, Opportunity, Accounting, Category


class IndexView(TemplateView):
    template_name = "index/index.html"
    try:

        def get(self, request, *args, **kwargs):
            self.extra_context = {
                "money_donated":
                    f'{Need.objects.filter(is_satisfied=True).aggregate(Sum("price")).get("price__sum"):,}'
                    .replace(",", " ")
                if (Need.objects.aggregate(Sum("price"))).get("price__sum")
                else 0,
                "number_of_requests": Need.objects.filter(is_satisfied=True).count(),
            }
            return self.render_to_response(self.extra_context)

    except (OperationalError, ProgrammingError):
        extra_context = {"money_donated": 0, "number_of_requests": 0}


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = "registration/user_form.html"
    success_url = reverse_lazy("core:core")

    def form_valid(self, form):
        print(self.kwargs)
        self.object = form.save(commit=True)
        self.object.is_active = True
        self.object.save()

        login(self.request, self.object, backend="core.auth_backend.AuthBackend")
        return HttpResponseRedirect(self.success_url)


class ChangePassword(SuccessMessageMixin, PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_message = "Password changed successfully!"
    success_url = reverse_lazy("core:core")


class ProfileView(LoginRequiredMixin, TemplateView):
    model = get_user_model()
    template_name = "accounts/profile.html"

    def get(self, request, *args, **kwargs):
        user_page = get_user_model().objects.get(pk=kwargs["pk"])
        needs = Need.objects.filter(author=kwargs["pk"])
        opportunities = Opportunity.objects.filter(author=kwargs["pk"])
        accounting = Accounting.objects.filter(author=kwargs["pk"])
        self.extra_context = {
            "user_page": user_page,
            "needs": needs,
            "opportunities": opportunities,
            "accounting": accounting,
        }

        return self.render_to_response(self.extra_context)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    user_type_fields = {
        "Single Volunteer": ["photo", "first_name", "last_name", "city"],
        "Volunteers Organisation": ["photo", "name", "city", "address"],
        "Civil Person": ["photo", "first_name", "last_name", "city"],
        "Military Person": ["photo", "unit"],
    }

    def get(self, request, *args, **kwargs):
        print(kwargs)
        self.fields = self.user_type_fields[get_user_model().objects.get(pk=kwargs["pk"]).type]
        return super().get(request, *args, **kwargs)


class NeededView(LoginRequiredMixin, TemplateView):
    model = get_user_model()
    template_name = "accounts/needed.html"

    def get(self, request, *args, **kwargs):
        needed = get_user_model().objects.filter(Q(type="Civil Person") | Q(type="Military Person"))
        self.extra_context = {"needed": needed}
        return self.render_to_response(self.extra_context)


class VolunteersView(LoginRequiredMixin, TemplateView):
    model = get_user_model()
    template_name = "accounts/volunteers.html"

    def get(self, request, *args, **kwargs):
        volunteers = get_user_model().objects.filter(Q(type="Single Volunteer") | Q(type="Volunteers Organisation"))
        self.extra_context = {"volunteers": volunteers}
        return self.render_to_response(self.extra_context)


# def UpdateProfilePhoto(request, pk):
#     if request.method == "POST":
#         image = request.FILES['fileToUpload']
#         print(image)
#         user_profile = Profile.objects.get(user=get_user_model().objects.get(pk=pk))
#         print(vars(user_profile))
#         user_profile.photo = image
#         user_profile.save()
#         print(vars(user_profile))
#         return HttpResponseRedirect(reverse_lazy("core:profile", kwargs={"pk": pk}))


class Login(LoginView):
    authentication_form = CustomAuthenticationForm
    next_page = reverse_lazy("core:core")


class Logout(LogoutView):
    next_page = reverse_lazy("core:core")


class NotFoundView(TemplateView):
    template_name = "index/404.html"


class ServerErrorView(TemplateView):
    template_name = "index/500.html"
