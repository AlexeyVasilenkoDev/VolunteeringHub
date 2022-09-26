from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [

    ]
    username = models.CharField(_("username"), max_length=150, )
    email = models.EmailField(_("email address"), null=True, blank=True, )
    phone = PhoneNumberField(_("phone"), null=True, blank=True, )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD =


class SingleVolunteerProfile(models.Model):
    pass


class VolunteersOrganisationProfile(models.Model):
    pass


class CivilPersonProfile(models.Model):
    pass


class MilitaryPersonProfile(models.Model):
    pass
