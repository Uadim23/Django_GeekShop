# Generated by Django 3.2.11 on 2022-02-12 00:08

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0005_create_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 0, 8, 14, 271745, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
