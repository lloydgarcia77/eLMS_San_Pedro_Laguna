# Generated by Django 3.1.2 on 2021-01-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elegislative_app', '0013_auto_20210122_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_arocc_manager',
            field=models.BooleanField(default=False, verbose_name='Can Manage Agenda, Resolution, Oridnance, Comments & Recommendation and Committee Reports'),
        ),
    ]
