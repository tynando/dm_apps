# Generated by Django 2.2.2 on 2019-07-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trapnet', '0031_auto_20190726_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='abbrev',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='abbreviation'),
        ),
    ]
