# Generated by Django 2.2.2 on 2019-11-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0048_auto_20191126_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='breakfast_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='breakfast rate (CAD/day)'),
        ),
        migrations.AddField(
            model_name='trip',
            name='incidental_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='incidental rate (CAD/day)'),
        ),
        migrations.AddField(
            model_name='trip',
            name='lunch_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='lunch rate (CAD/day)'),
        ),
        migrations.AddField(
            model_name='trip',
            name='no_incidentals',
            field=models.FloatField(blank=True, null=True, verbose_name='number of incidentals'),
        ),
        migrations.AddField(
            model_name='trip',
            name='supper_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='supper rate (CAD/day)'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='breakfasts',
            field=models.FloatField(blank=True, null=True, verbose_name='breakfasts'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='incidentals',
            field=models.FloatField(blank=True, null=True, verbose_name='incidentals'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='lunches',
            field=models.FloatField(blank=True, null=True, verbose_name='lunches'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='no_breakfasts',
            field=models.FloatField(blank=True, null=True, verbose_name='number of breakfasts'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='no_lunches',
            field=models.FloatField(blank=True, null=True, verbose_name='number of lunches'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='no_suppers',
            field=models.FloatField(blank=True, null=True, verbose_name='number of suppers'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='suppers',
            field=models.FloatField(blank=True, null=True, verbose_name='suppers'),
        ),
    ]
