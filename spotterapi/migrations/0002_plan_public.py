# Generated by Django 4.1.2 on 2022-11-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotterapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='public',
            field=models.BooleanField(default=1, verbose_name=False),
            preserve_default=False,
        ),
    ]
