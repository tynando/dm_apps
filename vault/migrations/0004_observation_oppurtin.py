# Generated by Django 2.2.2 on 2020-02-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0003_items_lending_quantity_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='oppurtin',
            field=models.BooleanField(default=False),
        ),
    ]
