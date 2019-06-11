# Generated by Django 2.1.4 on 2019-05-09 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0024_auto_20190509_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority_area_or_threat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='spot.PriorityAreaOrThreat'),
        ),
    ]