# Generated by Django 3.1.2 on 2021-01-13 04:38

from django.db import migrations, models
import django.db.models.deletion
import elegislative_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('elegislative_app', '0003_auto_20210112_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResolutionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('None', 'None'), ('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='None', max_length=100)),
                ('is_signed', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('hard_copy', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d', validators=[elegislative_app.models.file_validator_pdf], verbose_name='hard copy')),
                ('content', models.TextField()),
                ('date_filed', models.DateTimeField(auto_now=True)),
                ('agenda_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resolution_fk', to='elegislative_app.agendamodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrdinanceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('None', 'None'), ('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='None', max_length=100)),
                ('is_signed', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('hard_copy', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d', validators=[elegislative_app.models.file_validator_pdf], verbose_name='hard copy')),
                ('content', models.TextField()),
                ('date_filed', models.DateTimeField(auto_now=True)),
                ('ordinance_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordinance_fk', to='elegislative_app.agendamodel')),
            ],
        ),
    ]