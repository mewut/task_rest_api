# Generated by Django 5.0.2 on 2024-02-24 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('priority', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('title', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.executor')),
            ],
        ),
    ]
