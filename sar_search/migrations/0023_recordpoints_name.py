# Generated by Django 2.2.2 on 2019-08-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sar_search', '0022_auto_20190802_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordpoints',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='site name'),
        ),
    ]