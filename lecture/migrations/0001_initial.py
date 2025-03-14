# Generated by Django 3.0.5 on 2020-10-13 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapter', '0001_initial'),
        ('subjects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=288, verbose_name='Lecture Name')),
                ('type_of_lecture', models.CharField(choices=[('TEXT', 'text'), ('AUDIO', 'audio'), ('VIDEO', 'video')], default='TEXT', max_length=20, verbose_name='Lecture Type')),
                ('text', models.URLField(blank=True, max_length=255, null=True)),
                ('audio', models.URLField(blank=True, max_length=255, null=True)),
                ('video', models.URLField(blank=True, max_length=255, null=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapter.Chapter')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
