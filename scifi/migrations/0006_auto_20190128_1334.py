# Generated by Django 2.1.4 on 2019-01-28 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scifi', '0005_auto_20190128_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='fms_notes',
            new_name='mrs_notes',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='not_in_fms',
            new_name='not_in_mrs',
        ),
    ]