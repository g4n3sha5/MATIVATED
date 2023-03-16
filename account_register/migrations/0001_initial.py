# Generated by Django 4.1.2 on 2022-12-31 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('WorkoutJournal', '0002_trainingsession_techniques'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('bio', models.TextField(max_length=256)),
                ('belt', models.CharField(choices=[('NoInfo', 'NoInfo'), ('WhiteBelt', 'WhiteBelt'), ('BlueBelt', 'BlueBelt'), ('PurpleBelt', 'PurpleBelt'), ('BrownBelt', 'BrownBelt'), ('BlackBelt', 'BlackBelt')], max_length=16)),
                ('favGrappler', models.CharField(max_length=40)),
                ('favTechnique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutJournal.technique')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]