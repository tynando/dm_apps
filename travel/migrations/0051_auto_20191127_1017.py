# Generated by Django 2.2.2 on 2019-11-27 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0050_auto_20191127_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='location',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='location (city, province, country)'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='end date of travel'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shared_models.Section', verbose_name='DFO section'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start date of travel'),
        ),
    ]
