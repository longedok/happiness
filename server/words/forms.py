from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    AuthenticationForm as BaseAuthenticationForm,
)


class CustomFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            if visible.name in self.errors:
                visible.field.widget.attrs["class"] += " is-invalid"


class UserCreationForm(CustomFormMixin, BaseUserCreationForm):
    pass


class AuthenticationForm(CustomFormMixin, BaseAuthenticationForm):
    pass
