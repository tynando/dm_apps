# Generated by Django 2.2.2 on 2020-02-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0004_observation_oppurtin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lending',
            name='quantity_unique_id',
        ),
        migrations.RemoveField(
            model_name='quantity',
            name='items_quantity',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.AddField(
            model_name='observationplatform',
            name='longname',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='species',
            name='aphia_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID in World Registry of Marine Species'),
        ),
        migrations.AlterField(
            model_name='species',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Internal code'),
        ),
        migrations.AlterField(
            model_name='species',
            name='english_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='English name'),
        ),
        migrations.AlterField(
            model_name='species',
            name='french_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='French name'),
        ),
        migrations.AlterField(
            model_name='species',
            name='latin_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Scientific name'),
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Lending',
        ),
        migrations.DeleteModel(
            name='Quantity',
        ),
    ]
