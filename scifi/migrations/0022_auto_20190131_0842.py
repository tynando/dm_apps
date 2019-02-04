# Generated by Django 2.1.4 on 2019-01-31 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scifi', '0021_transaction_outstanding_obligation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['code']},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='responsibility_center',
            new_name='default_responsibility_center',
        ),
        migrations.AddField(
            model_name='transaction',
            name='responsibility_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='scifi.ResponsibilityCenter'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Expenditure'), (2, 'Adjustment'), (3, 'Allocation')], default=1),
        ),
    ]