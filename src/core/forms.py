from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from volunteering.models import Category


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["type", "username", "phone", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["type"].widget.attrs.update({"id": "type"})
        self.fields["username"].widget.attrs.update({"id": "username"})
        self.fields["phone"].widget.attrs.update({"id": "phone"})
        self.fields["email"].widget.attrs.update({"id": "email"})
        self.fields["password1"].widget.attrs.update({"id": "password1"})
        self.fields["password2"].widget.attrs.update({"id": "password2"})

    def clean(self):
        cleaned_data = super().clean()
        try:
            if (
                    not bool(cleaned_data["email"])
                    and not bool(cleaned_data["phone"])
                    and not bool(cleaned_data["username"])
            ):
                raise ValidationError("Insert some data for registering you, please")

            elif not bool(cleaned_data["email"]) and not bool(cleaned_data["username"]):
                if get_user_model().objects.filter(phone=cleaned_data["phone"]).exists():
                    raise ValidationError("User with this phone number already exists.")

            elif not bool(cleaned_data["phone"]) and not bool(cleaned_data["username"]):
                if get_user_model().objects.filter(email=cleaned_data["email"]).exists():
                    raise ValidationError("User with this email already exists.")

            elif not bool(cleaned_data["email"]) and not bool(cleaned_data["phone"]):
                if get_user_model().objects.filter(email=cleaned_data["username"]).exists():
                    raise ValidationError("User with this username already exists.")

        except KeyError:
            raise ValidationError("Enter a valid info please")

        return cleaned_data


class ProfileForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    print(get_user_model().type)


class CustomAuthenticationForm(AuthenticationForm):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    username = UsernameField(label="Email or Phone number", widget=forms.TextInput(attrs={"autofocus": True}))
