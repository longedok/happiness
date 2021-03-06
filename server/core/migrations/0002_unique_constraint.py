# Generated by Django 3.2.12 on 2022-04-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="userword",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="userword",
            constraint=models.UniqueConstraint(fields=("word", "user"), name="unique_user_word"),
        ),
    ]
