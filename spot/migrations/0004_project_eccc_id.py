# Generated by Django 2.1.4 on 2019-05-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0003_project_old_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='eccc_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
