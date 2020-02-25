# Generated by Django 2.2.2 on 2020-02-25 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisoryProcessType',
            fields=[
                ('apt_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='AptAdvisoryProcessType',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('apt_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CohHonorific',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('coh_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConContact',
            fields=[
                ('con_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='Some help here', max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('affiliation', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=255)),
                ('expertise', models.CharField(max_length=100)),
                ('cc_grad', models.BooleanField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CotType',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('cot_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilFile',
            fields=[
                ('fil_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FundingSource',
            fields=[
                ('fs_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='LanLanguage',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('lan_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocLocation',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('mct_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MctContactType',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('mct_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeqQuarter',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('meq_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetMeeting',
            fields=[
                ('met_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('title_en', models.CharField(max_length=255)),
                ('title_fr', models.CharField(max_length=255)),
                ('chair_comments', models.TextField(blank=True, null=True)),
                ('status_notes', models.TextField(blank=True, null=True)),
                ('lead_region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shared_models.Region')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.LocLocation')),
                ('process_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.AdvisoryProcessType')),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.MeqQuarter')),
            ],
        ),
        migrations.CreateModel(
            name='MftMeetingFileType',
            fields=[
                ('mft_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='NotNotificationPreference',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('not_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OmCategory',
            fields=[
                ('omc_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OthOther',
            fields=[
                ('oth_id', models.AutoField(primary_key=True, serialize=False)),
                ('oth_num', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='PsePublicationSeries',
            fields=[
                ('pse_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PubPublication',
            fields=[
                ('put_id', models.AutoField(primary_key=True, serialize=False)),
                ('pub_num', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ReqRequest',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('title_en', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RolRole',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScpScope',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('scp_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SecSector',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('sec_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SttStatus',
            fields=[
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_fr', models.CharField(max_length=255, unique=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('stt_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PubPublicationDetails',
            fields=[
                ('pub_id', models.AutoField(primary_key=True, serialize=False)),
                ('pub_year', models.IntegerField()),
                ('pub_number', models.CharField(max_length=25)),
                ('pages', models.IntegerField()),
                ('citation', models.TextField()),
                ('lead_author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.ConContact')),
                ('lead_region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shared_models.Region')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.LocLocation')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.ScpScope')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.PsePublicationSeries')),
            ],
        ),
        migrations.CreateModel(
            name='OmCost',
            fields=[
                ('om_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=20)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.OmCategory')),
                ('funding_source', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.FundingSource')),
            ],
        ),
        migrations.CreateModel(
            name='MomMeetingOmCost',
            fields=[
                ('mom_id', models.AutoField(primary_key=True, serialize=False)),
                ('met_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.MetMeeting')),
                ('om_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.OmCost')),
            ],
        ),
        migrations.AddField(
            model_name='metmeeting',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.ScpScope'),
        ),
        migrations.AddField(
            model_name='metmeeting',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.SttStatus'),
        ),
        migrations.CreateModel(
            name='MerOtherRegion',
            fields=[
                ('mer_id', models.AutoField(primary_key=True, serialize=False)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.MetMeeting')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shared_models.Region')),
            ],
        ),
        migrations.CreateModel(
            name='MepExpectedPublication',
            fields=[
                ('mep_id', models.AutoField(primary_key=True, serialize=False)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.MetMeeting')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.PubPublicationDetails')),
            ],
        ),
        migrations.CreateModel(
            name='MefMeetingFile',
            fields=[
                ('mef_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_en', models.IntegerField()),
                ('date_submitted', models.DateField(blank=True, null=True, verbose_name='Date Submitted')),
                ('date_posted', models.DateField(blank=True, null=True, verbose_name='Date Postted')),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.MftMeetingFileType')),
                ('file_fr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.FilFile')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.MetMeeting')),
            ],
        ),
        migrations.CreateModel(
            name='MecMeetingContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mec_id', models.CharField(max_length=45)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.ConContact')),
                ('contact_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.MctContactType')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.MetMeeting')),
            ],
        ),
        migrations.AddField(
            model_name='concontact',
            name='contact_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.CotType'),
        ),
        migrations.AddField(
            model_name='concontact',
            name='honorific',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.CohHonorific'),
        ),
        migrations.AddField(
            model_name='concontact',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.LanLanguage'),
        ),
        migrations.AddField(
            model_name='concontact',
            name='notification_preference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.NotNotificationPreference'),
        ),
        migrations.AddField(
            model_name='concontact',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shared_models.Region'),
        ),
        migrations.AddField(
            model_name='concontact',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.RolRole'),
        ),
        migrations.AddField(
            model_name='concontact',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='csas.SecSector'),
        ),
    ]
