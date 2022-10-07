from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["phone", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        try:
            if not bool(cleaned_data['email']) and not bool(cleaned_data['phone']):
                raise ValidationError("Insert email or phone number. At least one of them, please")

            elif not bool(cleaned_data['email']):
                if get_user_model().objects.filter(phone=cleaned_data['phone']).exists():
                    raise ValidationError("User with this phone number is exist.")

            elif not bool(cleaned_data['phone_number']):
                if get_user_model().objects.filter(email=cleaned_data['email']).exists():
                    raise ValidationError("User with this email is exist.")
        except KeyError:
            raise ValidationError("Enter a valid info please")

        return cleaned_data


class CustomAuthenticationForm(AuthenticationForm):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    username = UsernameField(label="Email or Phone number", widget=forms.TextInput(attrs={"autofocus": True}))
