# Generated by Django 4.2.7 on 2023-12-03 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Name is Used ,it must be Unique'}, max_length=50, unique=True, verbose_name='Name')),
                ('native', models.CharField(blank=True, error_messages={'unique': 'Native Name is Used ,it must be Unique'}, max_length=20, null=True, unique=True, verbose_name='Native')),
                ('iso_639_1', models.CharField(max_length=2, unique=True, verbose_name='ISO 639-1')),
                ('iso_639_2T', models.CharField(max_length=3, unique=True, verbose_name='ISO 639-2/T')),
                ('is_bidi', models.BooleanField(default=False, verbose_name='is Bidirectional Language')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
    ]
