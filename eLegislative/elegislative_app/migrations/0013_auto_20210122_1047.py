# Generated by Django 3.1.2 on 2021-01-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elegislative_app', '0012_auto_20210122_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationsmodel',
            name='tags',
            field=models.CharField(choices=[('None', 'None'), ('Agenda', 'Agenda'), ('Resolution', 'Resolution'), ('Ordinance', 'Ordinance'), ('MOM', 'MOM'), ('CRO', 'CRO'), ('CRR', 'CRR'), ('CMRO', 'CMRO'), ('CMRR', 'CMRR'), ('Announcement', 'Announcement')], default='None', max_length=250),
        ),
    ]
