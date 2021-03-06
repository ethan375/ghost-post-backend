# Generated by Django 3.0.2 on 2020-01-04 06:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boast', models.BooleanField()),
                ('body', models.CharField(max_length=280)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('creation_time', models.DateTimeField(default=datetime.datetime(2020, 1, 4, 6, 30, 29, 401592, tzinfo=utc))),
            ],
        ),
    ]
