# Generated by Django 3.2.15 on 2022-08-10 06:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LastUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(default=datetime.datetime(2022, 8, 10, 6, 31, 43, 248995, tzinfo=utc), verbose_name='last db update')),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_user_id', models.CharField(blank=True, max_length=124, null=True, verbose_name='id from the data')),
                ('first_name', models.CharField(blank=True, max_length=124, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=124, null=True, verbose_name='last name')),
                ('births', models.IntegerField(blank=True, null=True, verbose_name='birth seconds')),
                ('user_image_path', models.CharField(blank=True, max_length=124, null=True, verbose_name='path to the image file')),
            ],
        ),
    ]