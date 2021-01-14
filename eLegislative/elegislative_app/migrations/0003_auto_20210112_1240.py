# Generated by Django 3.1.2 on 2021-01-12 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elegislative_app', '0002_agendamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamodel',
            name='status',
            field=models.CharField(choices=[('None', 'None'), ('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='None', max_length=100),
        ),
    ]
