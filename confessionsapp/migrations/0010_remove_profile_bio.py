# Generated by Django 4.1 on 2022-10-04 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confessionsapp', '0009_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]