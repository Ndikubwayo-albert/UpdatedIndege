# Generated by Django 4.1.2 on 2022-12-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkerapp', '0004_alter_employer_passwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='passwd',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
