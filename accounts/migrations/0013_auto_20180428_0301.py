# Generated by Django 2.0.4 on 2018-04-28 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180428_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='instructor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='normal',
            field=models.BooleanField(default=True),
        ),
    ]
