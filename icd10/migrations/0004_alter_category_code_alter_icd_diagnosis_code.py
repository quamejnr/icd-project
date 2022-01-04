# Generated by Django 4.0 on 2022-01-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icd10', '0003_alter_icd_full_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='icd',
            name='diagnosis_code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]