# Generated by Django 3.2.12 on 2022-03-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_auto_20220313_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreboard',
            name='user_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='User title'),
        ),
    ]
