# Generated by Django 4.1.2 on 2023-02-26 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0022_rename_saturday_schedule_saturday_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='friday',
            new_name='Friday',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='monday',
            new_name='Monday',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='thursday',
            new_name='Thursday',
        ),
    ]