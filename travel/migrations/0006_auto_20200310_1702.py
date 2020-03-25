# Generated by Django 2.2.2 on 2020-03-10 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20200227_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='verified?'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trips_verified_by', to=settings.AUTH_USER_MODEL, verbose_name='verified by'),
        ),
    ]
