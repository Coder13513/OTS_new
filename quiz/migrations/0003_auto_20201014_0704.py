# Generated by Django 3.0.5 on 2020-10-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20201014_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='roll_out',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
