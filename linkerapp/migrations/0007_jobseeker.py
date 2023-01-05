# Generated by Django 4.1.2 on 2023-01-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkerapp', '0006_rename_passwd_employer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('card_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=5000)),
                ('firstname', models.CharField(max_length=5000)),
                ('lastname', models.CharField(max_length=5000)),
                ('phone', models.CharField(max_length=5000)),
                ('email', models.EmailField(max_length=5000)),
                ('gender', models.TextField()),
                ('indege_location', models.TextField()),
                ('job_type', models.TextField()),
                ('other_job', models.TextField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]