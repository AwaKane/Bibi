# Generated by Django 4.2.2 on 2023-06-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]