# Generated by Django 4.1.2 on 2023-01-30 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.AddField(
            model_name='notification',
            name='userReceiver',
            field=models.ManyToManyField(blank=True, related_name='userReceiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='userSender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userSender', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
