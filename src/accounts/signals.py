from accounts.models import Profile


def create_user_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
