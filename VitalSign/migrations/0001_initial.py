# Generated by Django 4.2.7 on 2023-12-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VitalSign',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Name is Used ,it must be Unique'}, max_length=50, unique=True, verbose_name='Name')),
                ('translations', models.JSONField(blank=True, null=True, verbose_name='Translations')),
                ('min_normal', models.FloatField(blank=True, null=True, verbose_name='Minmum Normal Value')),
                ('max_normal', models.FloatField(blank=True, null=True, verbose_name='Maximum Normal Value')),
                ('unit', models.CharField(blank=True, choices=[('m', 'mg/dL.')], max_length=10, null=True, verbose_name='Unit')),
            ],
            options={
                'verbose_name': 'Vital Sign',
                'verbose_name_plural': 'Vital Signs',
            },
        ),
    ]
