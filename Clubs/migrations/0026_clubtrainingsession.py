# Generated by Django 4.1.2 on 2023-03-18 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutJournal', '0009_remove_trainingsession_addedbyuser_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clubs', '0025_rename_field_schedule_friday_schedule_monday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubTrainingSession',
            fields=[
                ('trainingsession_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WorkoutJournal.trainingsession')),
                ('Club', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Clubs.club')),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('WorkoutJournal.trainingsession',),
        ),
    ]
