from django.contrib import admin

from server.users.models import User


@admin.register(User)
class WordAdmin(admin.ModelAdmin[User]):
    """Admin panel for `Word` model."""
    pass
