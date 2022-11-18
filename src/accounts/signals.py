from accounts.models import CustomProfile


def create_user_profile_signal(sender, instance, created, **kwargs):
    if created:
        CustomProfile.objects.create(photo="default_photo.jpg", user=instance)
