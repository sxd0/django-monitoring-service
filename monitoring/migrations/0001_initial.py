# Generated by Django 5.1.6 on 2025-02-12 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('ip_address', models.GenericIPAddressField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(max_length=10)),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.machine')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.FloatField()),
                ('mem', models.FloatField()),
                ('disk', models.FloatField()),
                ('uptime', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.machine')),
            ],
        ),
    ]
