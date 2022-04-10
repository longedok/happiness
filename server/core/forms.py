from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    AuthenticationForm as BaseAuthenticationForm,
    UsernameField,
)
from server.users.models import User


class CustomFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            if visible.name in self.errors:
                visible.field.widget.attrs["class"] += " is-invalid"


class UserCreationForm(CustomFormMixin, BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.is_active = False
        if commit:
            user.save()
        return user


class AuthenticationForm(CustomFormMixin, BaseAuthenticationForm):
    pass
