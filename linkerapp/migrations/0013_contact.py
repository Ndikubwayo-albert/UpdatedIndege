# Generated by Django 4.1.2 on 2023-01-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkerapp', '0012_remove_rfidcard_time_alter_rfidcard_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=5000)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=5000)),
                ('location', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
    ]
