# Generated by Django 2.2.2 on 2019-10-03 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_remove_milestone_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='milestoneprogressupdate',
            options={},
        ),
        migrations.RemoveField(
            model_name='milestoneprogressupdate',
            name='milestone',
        ),
        migrations.RemoveField(
            model_name='milestoneprogressupdate',
            name='status',
        ),
        migrations.RemoveField(
            model_name='milestoneprogressupdate',
            name='status_report',
        ),
    ]
