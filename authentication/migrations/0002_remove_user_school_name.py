# Generated by Django 3.0.5 on 2020-10-14 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='school_name',
        ),
    ]
