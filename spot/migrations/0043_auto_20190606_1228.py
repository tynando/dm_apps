# Generated by Django 2.1.4 on 2019-06-06 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0042_auto_20190605_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expressionofinterest',
            name='date_received',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date received'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='project_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='spot.ProjectYear'),
        ),
        migrations.AlterField(
            model_name='projectyear',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='years', to='spot.Project', verbose_name='project language'),
        ),
    ]