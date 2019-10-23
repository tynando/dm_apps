# Generated by Django 2.2.2 on 2019-07-25 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sar_search', '0003_county_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='range',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sar_sites', to='sar_search.County'),
        ),
    ]