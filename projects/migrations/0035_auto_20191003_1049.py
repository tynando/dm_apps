# Generated by Django 2.2.2 on 2019-10-03 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_auto_20191003_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='milestoneupdate',
            options={'ordering': ['-status_report', 'status']},
        ),
        migrations.AddField(
            model_name='milestoneupdate',
            name='milestone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='projects.Milestone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milestoneupdate',
            name='status',
            field=models.ForeignKey(default=9, limit_choices_to={'used_for': 3}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updates', to='projects.Status'),
        ),
        migrations.AddField(
            model_name='milestoneupdate',
            name='status_report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='projects.StatusReport'),
            preserve_default=False,
        ),
    ]
