# Generated by Django 4.1.5 on 2023-01-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]
