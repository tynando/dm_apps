# Generated by Django 2.2.2 on 2020-02-25 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20200221_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triprequest',
            name='accommodations',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='air',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='breakfasts',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='breakfasts_rate',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='incidentals',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='incidentals_rate',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='lunches',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='lunches_rate',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='no_breakfasts',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='no_incidentals',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='no_lunches',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='no_suppers',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='other',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='other_transport',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='personal_motor_vehicle',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='rail',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='registration',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='rental_motor_vehicle',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='suppers',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='suppers_rate',
        ),
        migrations.RemoveField(
            model_name='triprequest',
            name='taxi',
        ),
        migrations.AlterField(
            model_name='conference',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='trip title (English)'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='trip title (French)'),
        ),
        migrations.AlterField(
            model_name='triprequest',
            name='exclude_from_travel_plan',
            field=models.BooleanField(default=False, verbose_name='Exclude this traveller from the travel plan?'),
        ),
        migrations.AlterField(
            model_name='triprequest',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_requests', to='shared_models.Region', verbose_name='Traveller belongs to which DFO region'),
        ),
        migrations.AlterField(
            model_name='triprequest',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_requests', to='shared_models.Section', verbose_name='under which DFO section is this request being made'),
        ),
    ]
