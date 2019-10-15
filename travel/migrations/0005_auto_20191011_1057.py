# Generated by Django 2.2.2 on 2019-10-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_event_approver'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approver_approval_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expenditure initiation approval date'),
        ),
        migrations.AddField(
            model_name='event',
            name='recommender_1_approval_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='recommender 1 approval date'),
        ),
        migrations.AddField(
            model_name='event',
            name='recommender_2_approval_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='recommender 2 approval date'),
        ),
        migrations.AddField(
            model_name='event',
            name='recommender_3_approval_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='recommender 3 approval date'),
        ),
    ]
