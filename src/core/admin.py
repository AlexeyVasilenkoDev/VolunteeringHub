from django.contrib import admin  # NOQA

# Register your models here.
from accounts.models import (
    CustomUser,
)
from volunteering.models import Accounting, Category, Need, Opportunity
from accounts.models import Profile

admin.site.register(
    [
        CustomUser,
        Need,
        Opportunity,
        Category,
        Accounting,
        Profile
    ]
)
