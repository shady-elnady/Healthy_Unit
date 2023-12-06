# Generated by Django 4.2.7 on 2023-12-06 11:56

import Utils.models.Methods
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
        ('Address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Name is Used ,it must be Unique'}, max_length=50, unique=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Utils.models.Methods.upload_image_to, verbose_name='Image')),
                ('translations', models.JSONField(blank=True, null=True, verbose_name='Translations')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s+', to='Category.category', verbose_name='Category')),
                ('made_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Made_Brands', to='Address.country', verbose_name='Made In')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
    ]
