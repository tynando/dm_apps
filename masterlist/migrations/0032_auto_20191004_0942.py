# Generated by Django 2.2.2 on 2019-10-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0031_auto_20190930_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='abbrev',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='abbreviation'),
        ),
    ]