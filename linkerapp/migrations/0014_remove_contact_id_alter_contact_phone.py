# Generated by Django 4.1.2 on 2023-01-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkerapp', '0013_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
