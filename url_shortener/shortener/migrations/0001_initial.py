# Generated by Django 5.1.6 on 2025-03-04 05:22

import shortener.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2000)),
                ('short_code', models.CharField(default=shortener.models.generate_short_code, max_length=6, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('access_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
