# Generated by Django 2.1.4 on 2019-04-17 13:40

import dm_apps.custom_widgets
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20190417_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='title_eng',
            field=dm_apps.custom_widgets.OracleTextField(verbose_name='Title (English)'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='title_fre',
            field=dm_apps.custom_widgets.OracleTextField(blank=True, null=True, verbose_name='Title (French)'),
        ),
    ]
