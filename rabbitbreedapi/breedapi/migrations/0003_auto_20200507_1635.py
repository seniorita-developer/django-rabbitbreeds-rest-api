# Generated by Django 3.0.6 on 2020-05-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breedapi', '0002_auto_20200507_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='image',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]