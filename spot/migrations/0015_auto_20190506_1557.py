# Generated by Django 2.1.4 on 2019-05-06 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0014_auto_20190506_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='hsp_id',
            new_name='program_reference_number',
        ),
    ]
