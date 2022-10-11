from django.contrib import admin  # NOQA

# Register your models here.
from accounts.models import (
    CustomUser,
    SingleVolunteerProfile,
    VolunteersOrganisationProfile,
    CivilPersonProfile,
    MilitaryPersonProfile,
)
from volunteering.models import Accounting, Need, Opportunity, Category

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
