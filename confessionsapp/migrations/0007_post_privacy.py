# Generated by Django 4.1 on 2022-10-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confessionsapp', '0006_subjectpage_title_alter_subjectpage_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='privacy',
            field=models.CharField(default='show', max_length=10),
        ),
    ]
