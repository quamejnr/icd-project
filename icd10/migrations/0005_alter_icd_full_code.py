# Generated by Django 4.0 on 2022-03-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icd10', '0004_alter_category_code_alter_icd_diagnosis_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icd',
            name='full_code',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
