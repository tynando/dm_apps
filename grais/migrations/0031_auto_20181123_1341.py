# Generated by Django 2.0.4 on 2018-11-23 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grais', '0030_auto_20181123_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplespecies',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sample_spp', to='grais.Species'),
        ),
    ]