# Generated by Django 2.1.4 on 2019-03-21 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20190321_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='section',
            name='unit_head',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
