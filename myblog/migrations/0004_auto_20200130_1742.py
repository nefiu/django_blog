# Generated by Django 3.0.2 on 2020-01-30 17:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20200130_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 17, 42, 53, 414048, tzinfo=utc)),
        ),
    ]