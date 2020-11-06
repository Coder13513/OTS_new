# Generated by Django 3.0.5 on 2020-10-13 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_ukg_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_nursery_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_lkg_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_9_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_8_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_7_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_6_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_5_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_4_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_3_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_2_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_1_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_10_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='class 1', editable=False, max_length=200)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
