# Generated by Django 4.1.2 on 2023-03-18 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutJournal', '0011_trainingsession_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingsession',
            name='club',
        ),
        migrations.RemoveField(
            model_name='trainingsession',
            name='participants',
        ),
    ]
