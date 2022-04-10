from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Word
from .tasks import fetch_oxford_data as fetch_oxford_data_task


@receiver(post_save, sender=Word)
def fetch_oxford_data(sender, instance, **kwargs):
    if kwargs.get("created"):
        transaction.on_commit(lambda: fetch_oxford_data_task.delay(instance.id))
