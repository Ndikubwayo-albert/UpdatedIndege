# Generated by Django 4.1.2 on 2023-01-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkerapp', '0008_remove_jobseeker_username_jobseeker_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='job_type',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
