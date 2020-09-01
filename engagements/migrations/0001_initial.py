# Generated by Django 2.2.2 on 2020-08-17 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared_models', '0007_auto_20200617_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(max_length=127)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('fax_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('webpage', models.URLField(blank=True)),
                ('business_number', models.CharField(blank=True, max_length=12, verbose_name='CRA Business Number')),
                ('address_line_1', models.CharField(blank=True, max_length=31)),
                ('address_line_2', models.CharField(blank=True, max_length=31)),
                ('city', models.CharField(blank=True, max_length=15)),
                ('zip_postal', models.CharField(blank=True, max_length=10, verbose_name='ZIP/Postal Code')),
                ('country', models.CharField(blank=True, default='Canada', max_length=50)),
                ('organization_type', models.CharField(blank=True, choices=[('', '----'), ('Federal Government', 'Federal Government'), ('Provincial/State Government', 'Provincial/State Government'), ('Municipal Government', 'Municipal Government'), ('Indigenous Group/Government', 'Indigenous Group/Government'), ('Association', 'Association'), ('Small and Medium-Sized Business', 'Small and Medium-Sized Business'), ('Multinational Enterprise', 'Multinational Enterprise'), ('Accelerator/Incubator/Network', 'Accelerator/Incubator/Network'), ('PSI', 'Post-Secondary Institution'), ('Other', 'Other')], default='', max_length=50)),
                ('other_organization_type', models.CharField(blank=True, max_length=50)),
                ('profit_nonprofit', models.PositiveIntegerField(blank=True, choices=[(None, '----'), (1, 'Profit'), (0, 'Non-Profit')], default=None, verbose_name='Profit/Non-Profit')),
                ('stakeholder_type', models.PositiveIntegerField(choices=[(1, 'Internal'), (2, 'Government of Canada'), (3, 'External')], default=3)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=127)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_organizations', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_organizations', to=settings.AUTH_USER_MODEL)),
                ('parent_organizations', models.ManyToManyField(blank=True, related_name='_organization_parent_organizations_+', to='engagements.Organization')),
                ('province', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='organizations', to='shared_models.Province')),
            ],
        ),
    ]