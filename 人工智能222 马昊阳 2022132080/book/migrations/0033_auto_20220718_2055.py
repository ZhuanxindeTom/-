# Generated by Django 2.2.10 on 2022-07-18 12:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0032_auto_20220717_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 25, 12, 55, 44, 244579, tzinfo=utc)),
        ),
    ]
