# Generated by Django 2.2.2 on 2019-07-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20190702_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]