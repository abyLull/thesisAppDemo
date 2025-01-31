# Generated by Django 5.0.4 on 2024-07-29 10:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(choices=[('Wydział Administracji i Nauk Społecznych', 'Wydział Administracji i Nauk Społecznych'), ('Wydział Architektury', 'Wydział Architektury'), ('none', 'None')], default='None', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('year_of_study', models.PositiveIntegerField()),
                ('contract_codes', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='Pending', max_length=50)),
                ('year', models.CharField(default='2024', max_length=4)),
                ('faculty', models.CharField(choices=[('Wydział Administracji i Nauk Społecznych', 'Wydział Administracji i Nauk Społecznych'), ('Wydział Architektury', 'Wydział Architektury'), ('none', 'None')], default='None', max_length=100)),
                ('comment', models.TextField(default='None')),
                ('study_level', models.CharField(default='Not Provided', max_length=20)),
                ('gpa', models.FloatField(blank=True, default=0, null=True)),
                ('modified', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], default='negative', max_length=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=100)),
                ('available_places', models.PositiveIntegerField()),
                ('contract_code', models.CharField(max_length=25)),
                ('year', models.CharField(default='2024', max_length=4)),
                ('faculty', models.CharField(choices=[('Wydział Administracji i Nauk Społecznych', 'Wydział Administracji i Nauk Społecznych'), ('Wydział Architektury', 'Wydział Architektury'), ('none', 'None')], default='None', max_length=100)),
                ('study_level_available', models.CharField(default='Not Provided', max_length=50)),
                ('comment', models.TextField(default='None')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to=settings.AUTH_USER_MODEL)),
                ('student', models.ManyToManyField(blank=True, null=True, to='api.student')),
            ],
        ),
    ]
