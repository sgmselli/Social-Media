# Generated by Django 4.1 on 2022-10-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confessionsapp', '0003_likepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.CharField(default='general', max_length=40),
        ),
    ]
