# Generated by Django 3.2.12 on 2022-04-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_name",
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, max_length=150, verbose_name="name"),
        ),
        migrations.AlterModelTable(
            name="user",
            table=None,
        ),
    ]
