# Generated by Django 4.2.7 on 2023-12-06 11:56

from django.db import migrations, models
import django.db.models.deletion
import polymorphic_tree.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0002_initial'),
        ('Service', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='User.profile', verbose_name='Patient'),
        ),
        migrations.AddField(
            model_name='servicerecord',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='servicerecord',
            name='service',
            field=models.ForeignKey(limit_choices_to={'parent__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='Service.service', verbose_name='Service'),
        ),
        migrations.AddField(
            model_name='service',
            name='parent',
            field=polymorphic_tree.models.PolymorphicTreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='Service.service', verbose_name='Parent'),
        ),
        migrations.AddField(
            model_name='service',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='parentservice',
            name='managing_director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='Employee.employee', verbose_name='Managing Director'),
        ),
    ]
