# Generated by Django 5.1.6 on 2025-03-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_remove_resume_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
