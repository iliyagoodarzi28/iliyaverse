# Generated by Django 5.1.6 on 2025-03-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_resume_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='مهارت ها')),
            ],
        ),
        migrations.RemoveField(
            model_name='resume',
            name='skill',
        ),
    ]
