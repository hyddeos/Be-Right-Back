# Generated by Django 4.1.3 on 2022-11-21 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brb', '0004_alter_away_return_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='away',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
