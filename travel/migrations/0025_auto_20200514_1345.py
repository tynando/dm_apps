# Generated by Django 2.2.2 on 2020-05-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0024_auto_20200513_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripsubcategory',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
