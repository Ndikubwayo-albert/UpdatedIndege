# Generated by Django 4.1.2 on 2023-01-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkerapp', '0015_remove_rfidcard_date_rfidcard_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Present_worker',
            fields=[
                ('card_id', models.IntegerField(primary_key=True, serialize=False)),
                ('arrival_time', models.TimeField(auto_now_add=True)),
                ('names', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('work_type', models.CharField(max_length=5000)),
                ('location', models.TextField()),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]
