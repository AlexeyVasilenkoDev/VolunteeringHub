from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model()


class AuthBackend(ModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, request, login_field=None, password=None, **kwargs):
        # if username is None:
        #     username = kwargs.get(UserModel.USERNAME_FIELD)
        if login_field is None or password is None:
            return
        try:
            user = UserModel.objects.get(
                Q(username=login_field) | Q(email=login_field) | Q(phone=login_field)
            )
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
