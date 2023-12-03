# Generated by Django 4.2.7 on 2023-12-03 15:53

import Utils.models.Methods
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radiology',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Service.service')),
            ],
            options={
                'verbose_name': 'Radiology',
                'verbose_name_plural': 'Radiologies',
            },
            bases=('Service.service',),
        ),
        migrations.CreateModel(
            name='RadiologySession',
            fields=[
                ('servicerecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Service.servicerecord')),
            ],
            options={
                'verbose_name': 'Radiology Session',
                'verbose_name_plural': 'Radiologies Sessions',
            },
            bases=('Service.servicerecord',),
        ),
        migrations.CreateModel(
            name='RadiologyImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Utils.models.Methods.upload_image_to, verbose_name='Image')),
                ('RadiologySession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Radiologies_Images', to='Radiology.radiologysession', verbose_name='Radiology Session')),
            ],
            options={
                'verbose_name': 'Radiology Image',
                'verbose_name_plural': 'Radiologies Images',
            },
        ),
    ]
