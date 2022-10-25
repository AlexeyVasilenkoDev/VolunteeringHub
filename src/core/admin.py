from django.contrib import admin  # NOQA

# Register your models here.
from accounts.models import (
    CivilPersonProfile,
    CustomUser,
    MilitaryPersonProfile,
    SingleVolunteerProfile,
    VolunteersOrganisationProfile,
)
from volunteering.models import Accounting, Category, Need, Opportunity

admin.site.register(
    [
        CustomUser,
        SingleVolunteerProfile,
        VolunteersOrganisationProfile,
        CivilPersonProfile,
        MilitaryPersonProfile,
        Need,
        Opportunity,
        Category,
        Accounting,
    ]
)
