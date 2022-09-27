from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import CustomerManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class UserTypeChoices(models.TextChoices):
        SINGLE_VOLUNTEER = 'Single Volunteer', _('Single Volunteer')
        VOLUNTEERS_ORGANISATION = 'Volunteers Organisation', _('Volunteers Organisation')
        CIVIL_PERSON = 'Civil Person', _('Civil Person')
        MILITARY_PERSON = 'Military Person', _('Military Person')

    type = models.CharField(
        max_length=23,
        choices=UserTypeChoices.choices,
    )
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

    USERNAME_FIELD = 'email'

    objects = CustomerManager()


class CustomProfile(models.Model):
    user = models.ForeignKey(to="accounts.CustomUser", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


class SingleVolunteerProfile(CustomProfile):
    opportunity = models.ManyToManyField(to="volunteering.Opportunity")


class VolunteersOrganisationProfile(CustomProfile):
    opportunity = models.ManyToManyField(to="volunteering.Opportunity")


class CivilPersonProfile(CustomProfile):
    need = models.ManyToManyField(to="volunteering.Need")


class MilitaryPersonProfile(CustomProfile):
    need = models.ManyToManyField(to="volunteering.Need")
