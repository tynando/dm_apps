# Generated by Django 2.2.2 on 2020-05-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmutools', '0017_auto_20200508_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='comments/details'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='website',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='comments/details'),
        ),
    ]