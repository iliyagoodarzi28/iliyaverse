# Generated by Django 5.1.6 on 2025-03-17 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_resume_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='slug',
        ),
    ]
