# Generated by Django 3.0.2 on 2020-01-04 07:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ghosting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 4, 7, 11, 9, 20536, tzinfo=utc)),
        ),
    ]
