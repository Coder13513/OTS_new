# Generated by Django 3.0.5 on 2020-10-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=288, verbose_name='Lecture Name'),
        ),
    ]
