# Generated by Django 2.2.2 on 2019-07-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sar_search', '0002_auto_20190725_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='code',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]