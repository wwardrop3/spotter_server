# Generated by Django 4.1.2 on 2022-11-02 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotterapi', '0002_plan_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='from_plan',
            field=models.BooleanField(default=1, verbose_name=True),
            preserve_default=False,
        ),
    ]