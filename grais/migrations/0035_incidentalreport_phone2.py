# Generated by Django 2.1.4 on 2019-02-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grais', '0034_auto_20190215_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentalreport',
            name='phone2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
