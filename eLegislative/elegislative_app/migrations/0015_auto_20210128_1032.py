# Generated by Django 3.1.2 on 2021-01-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elegislative_app', '0014_user_is_arocc_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_announcement_manager',
            field=models.BooleanField(default=False, verbose_name='Can Manage Announcement'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_mom_manager',
            field=models.BooleanField(default=False, verbose_name='Can Manage Minutes of the Meeting'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_old_documents_manager',
            field=models.BooleanField(default=False, verbose_name='Can Manage/Upload Old/Existing Oridnance.'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_records_manager',
            field=models.BooleanField(default=False, verbose_name='Can Manager Records'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_webex_manager',
            field=models.BooleanField(default=False, verbose_name='Can Manage External Links from Webex for Reviewing.'),
        ),
    ]
