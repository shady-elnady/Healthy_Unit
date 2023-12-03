# Generated by Django 4.2.7 on 2023-12-03 17:18

import Utils.Custom_Fields
import Utils.models.Methods
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Currency', '0001_initial'),
        ('Brand', '0001_initial'),
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Name is Used ,it must be Unique'}, max_length=50, unique=True, verbose_name='Name')),
                ('translations', models.JSONField(blank=True, null=True, verbose_name='Translations')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='Brand.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(limit_choices_to={'category_parent__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='Category.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Drug',
                'verbose_name_plural': 'Drugs',
            },
        ),
        migrations.CreateModel(
            name='PharmaceuticalForm',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Name is Used ,it must be Unique'}, max_length=50, unique=True, verbose_name='Name')),
                ('translations', models.JSONField(blank=True, null=True, verbose_name='Translations')),
            ],
            options={
                'verbose_name': 'Pharmaceutical Form',
                'verbose_name_plural': 'Pharmaceutical Forms',
            },
        ),
        migrations.CreateModel(
            name='DrugPacking',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('bar_code', Utils.Custom_Fields.BarCodeField(max_length=24, primary_key=True, serialize=False, verbose_name='BarCode')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Utils.models.Methods.upload_image_to, verbose_name='Image')),
                ('price', models.FloatField(verbose_name='Price')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s+', to='Currency.currency', verbose_name='Currency')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Drugs_Packing', to='Drug.drug', verbose_name='Drug')),
                ('pharmaceutical_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Drugs', to='Drug.pharmaceuticalform', verbose_name='Pharmaceutical Form')),
            ],
            options={
                'verbose_name': 'Drug Packing',
                'verbose_name_plural': 'Drugs Packings',
            },
        ),
        migrations.CreateModel(
            name='DrugEffectiveMaterial',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Name is Used ,it must be Unique'}, max_length=50, unique=True, verbose_name='Name')),
                ('translations', models.JSONField(blank=True, null=True, verbose_name='Translations')),
                ('for_child_pregnant', models.BooleanField(default=True, verbose_name='for Child Pregnant')),
                ('drug_effective_material_category', models.ForeignKey(limit_choices_to={'category_parent__name__isequ': 'Drug'}, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s+', to='Category.category', verbose_name='Drug Effective Material Category')),
            ],
            options={
                'verbose_name': 'Drug Effective Material',
                'verbose_name_plural': 'Drug Effective Materials',
            },
        ),
        migrations.AddField(
            model_name='drug',
            name='drug_effective_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='Drug.drugeffectivematerial', verbose_name='Drug Effective Material'),
        ),
    ]
