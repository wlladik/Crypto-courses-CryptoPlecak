# Generated by Django 5.0 on 2024-01-03 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_leson'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leson',
            new_name='Lesson',
        ),
    ]