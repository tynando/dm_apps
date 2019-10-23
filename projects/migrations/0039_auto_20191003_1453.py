# Generated by Django 2.2.2 on 2019-10-03 17:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0038_auto_20191003_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='external_url',
            field=models.URLField(blank=True, null=True, verbose_name='external URL'),
        ),
        migrations.AlterUniqueTogether(
            name='staff',
            unique_together={('project', 'user')},
        ),
    ]