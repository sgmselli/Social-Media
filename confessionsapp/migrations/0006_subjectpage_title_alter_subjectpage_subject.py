# Generated by Django 4.1 on 2022-10-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confessionsapp', '0005_subjectpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectpage',
            name='title',
            field=models.CharField(default='General', max_length=40),
        ),
        migrations.AlterField(
            model_name='subjectpage',
            name='subject',
            field=models.CharField(default='general', max_length=40),
        ),
    ]
