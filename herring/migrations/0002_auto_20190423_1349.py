# Generated by Django 2.1.4 on 2019-04-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='alias_port_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='alias_wharf_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
