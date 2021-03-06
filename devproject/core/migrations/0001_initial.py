# Generated by Django 3.0.8 on 2020-07-30 02:29

import devproject.core.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_id', models.BigIntegerField(unique=True, verbose_name='Github ID')),
                ('github_node_id', models.CharField(max_length=50, unique=True, verbose_name='Github Node ID')),
                ('created_at', models.DateTimeField(editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(editable=False, verbose_name='Updated at')),
                ('url', models.URLField(editable=False, max_length=1000, verbose_name='URL')),
                ('raw', django.contrib.postgres.fields.jsonb.JSONField(editable=False, verbose_name='Raw')),
                ('login', models.CharField(max_length=100, unique=True, verbose_name='Login')),
                ('avatar_url', models.URLField(blank=True, null=True, verbose_name='Avatar URL')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('company', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company')),
                ('location', models.CharField(blank=True, max_length=250, null=True, verbose_name='Location')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, unique=True, verbose_name='E-mail')),
                ('hireable', models.BooleanField(blank=True, null=True, verbose_name='Can be hired?')),
                ('bio', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Biography')),
            ],
            options={
                'verbose_name': 'developer',
                'verbose_name_plural': 'developers',
            },
            bases=(devproject.core.models.ValidateOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_id', models.BigIntegerField(unique=True, verbose_name='Github ID')),
                ('github_node_id', models.CharField(max_length=50, unique=True, verbose_name='Github Node ID')),
                ('created_at', models.DateTimeField(editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(editable=False, verbose_name='Updated at')),
                ('url', models.URLField(editable=False, max_length=1000, verbose_name='URL')),
                ('raw', django.contrib.postgres.fields.jsonb.JSONField(editable=False, verbose_name='Raw')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('full_name', models.CharField(max_length=250, unique=True, verbose_name='Full name')),
                ('private', models.BooleanField(blank=True, default=False, verbose_name='Private?')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
            bases=(devproject.core.models.ValidateOnSaveMixin, models.Model),
        ),
    ]
