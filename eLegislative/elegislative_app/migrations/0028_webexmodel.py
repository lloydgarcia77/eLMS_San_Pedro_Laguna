# Generated by Django 3.1.2 on 2021-02-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elegislative_app', '0027_auto_20210204_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebExModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('display_text', models.CharField(max_length=250)),
                ('protcol', models.CharField(choices=[('http://', 'http://'), ('https://', 'https://'), ('ftp://', 'ftp://'), ('news://', 'news://'), ('<other>', '<other>')], default='http://', max_length=50)),
                ('remarks', models.CharField(max_length=250)),
                ('date_filed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
