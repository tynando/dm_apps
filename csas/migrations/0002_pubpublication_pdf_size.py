# Generated by Django 2.2.2 on 2020-09-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubpublication',
            name='pdf_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='PDF Size'),
        ),
    ]
