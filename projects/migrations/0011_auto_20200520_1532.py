# Generated by Django 2.2.2 on 2020-05-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_notification_email_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='approved',
            field=models.NullBooleanField(default=False, verbose_name='approved'),
        ),
    ]