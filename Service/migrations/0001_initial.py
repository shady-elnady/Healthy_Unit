# Generated by Django 4.2.7 on 2023-12-06 11:56

import Utils.Custom_Fields
import Utils.models.Methods
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Name is Used ,it must be Unique'}, max_length=50, unique=True, verbose_name='Name')),
                ('translations', models.JSONField(blank=True, null=True, verbose_name='Translations')),
                ('content_type', models.CharField(editable=False, max_length=30, verbose_name='Content Types')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('bar_code', Utils.Custom_Fields.BarCodeField(max_length=24, primary_key=True, serialize=False, verbose_name='BarCode')),
                ('content_type', models.CharField(editable=False, max_length=30, verbose_name='Content Types')),
                ('diagnosis', models.TextField(blank=True, max_length=500, null=True, verbose_name='Diagnosis')),
                ('note', models.TextField(verbose_name='Note')),
            ],
            options={
                'verbose_name': 'Service Record',
                'verbose_name_plural': 'Services Records',
            },
        ),
        migrations.CreateModel(
            name='ParentService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Service.service')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Utils.models.Methods.upload_image_to, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Parent Service',
                'verbose_name_plural': 'Parent Services',
            },
            bases=('Service.service', models.Model),
        ),
    ]
