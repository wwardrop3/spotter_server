# Generated by Django 4.1.2 on 2022-11-02 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotterapi', '0004_remove_session_from_plan_remove_session_profile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='exercises',
            new_name='session_exercises',
        ),
    ]
