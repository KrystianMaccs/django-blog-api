# Generated by Django 3.2.7 on 2022-07-20 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country_geoname_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='joined_on_holiday',
        ),
        migrations.RemoveField(
            model_name='user',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='user',
            name='longitude',
        ),
    ]
