# Generated by Django 4.0.1 on 2022-01-11 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestion',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 14, 46, 42, 153605, tzinfo=utc)),
        ),
    ]
