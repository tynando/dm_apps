# Generated by Django 2.2.2 on 2019-11-20 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrsCruises',
            fields=[
                ('crs_id', models.AutoField(primary_key=True, serialize=False)),
                ('crs_name', models.CharField(max_length=50, unique=True)),
                ('crs_pi_name', models.CharField(blank=True, max_length=50, null=True)),
                ('crs_institute_name', models.CharField(blank=True, max_length=50, null=True)),
                ('crs_geographic_location', models.CharField(blank=True, max_length=50, null=True)),
                ('crs_start_date', models.DateField(blank=True, null=True)),
                ('crs_end_date', models.DateField(blank=True, null=True)),
                ('crs_notes', models.CharField(blank=True, max_length=4000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepDeployments',
            fields=[
                ('dep_id', models.AutoField(primary_key=True, serialize=False)),
                ('dep_year', models.BigIntegerField()),
                ('dep_month', models.BigIntegerField()),
                ('dep_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EcaCalibrationEvent',
            fields=[
                ('eca_id', models.AutoField(primary_key=True, serialize=False)),
                ('eca_date', models.DateField()),
                ('eca_notes', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmmMakeModel',
            fields=[
                ('emm_id', models.AutoField(primary_key=True, serialize=False)),
                ('emm_make', models.CharField(max_length=50)),
                ('emm_model', models.CharField(max_length=50)),
                ('emm_depth_rating', models.BigIntegerField()),
                ('emm_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EqaAdcBitsCode',
            fields=[
                ('eqa_id', models.AutoField(primary_key=True, serialize=False)),
                ('eqa_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EqtEquipmentTypeCode',
            fields=[
                ('eqt_id', models.AutoField(primary_key=True, serialize=False)),
                ('eqt_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MorMooringSetups',
            fields=[
                ('mor_id', models.AutoField(primary_key=True, serialize=False)),
                ('mor_name', models.CharField(max_length=50, unique=True)),
                ('mor_max_depth', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('mor_link_setup_image', models.CharField(blank=True, max_length=4000, null=True)),
                ('mor_additional_equipment', models.CharField(blank=True, max_length=4000, null=True)),
                ('mor_general_moor_description', models.CharField(blank=True, max_length=4000, null=True)),
                ('more_notes', models.CharField(blank=True, max_length=4000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrjProjects',
            fields=[
                ('prj_id', models.AutoField(primary_key=True, serialize=False)),
                ('prj_name', models.CharField(max_length=255, unique=True)),
                ('prj_descrption', models.CharField(blank=True, max_length=4000, null=True)),
                ('prj_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrmParameterCode',
            fields=[
                ('prm_id', models.AutoField(primary_key=True, serialize=False)),
                ('prm_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RscRecordingSchedules',
            fields=[
                ('rsc_id', models.AutoField(primary_key=True, serialize=False)),
                ('rsc_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rsc_period', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RttTimezoneCode',
            fields=[
                ('rtt_id', models.AutoField(primary_key=True, serialize=False)),
                ('rtt_abb', models.CharField(max_length=5)),
                ('rtt_name', models.CharField(max_length=50)),
                ('rtt_offset', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='SetStationEventCode',
            fields=[
                ('set_id', models.AutoField(primary_key=True, serialize=False)),
                ('set_name', models.CharField(max_length=50, unique=True)),
                ('set_description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='StnStations',
            fields=[
                ('stn_id', models.AutoField(primary_key=True, serialize=False)),
                ('stn_name', models.CharField(max_length=100)),
                ('stn_code', models.CharField(max_length=3)),
                ('stn_revision', models.BigIntegerField()),
                ('stn_planned_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('stn_planned_lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('stn_planned_depth', models.DecimalField(decimal_places=6, max_digits=10)),
                ('stn_notes', models.CharField(blank=True, max_length=4000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EqhHydrophoneProperties',
            fields=[
                ('emm', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='whalesdb.EmmMakeModel')),
                ('eqh_range_min', models.BigIntegerField()),
                ('eqh_range_max', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeaTeamMembers',
            fields=[
                ('tea_id', models.AutoField(primary_key=True, serialize=False)),
                ('tea_abb', models.CharField(blank=True, max_length=50, null=True)),
                ('tea_last_name', models.CharField(max_length=50)),
                ('tea_first_name', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('tea_last_name', 'tea_first_name')},
            },
        ),
        migrations.CreateModel(
            name='SteStationEvents',
            fields=[
                ('ste_id', models.AutoField(primary_key=True, serialize=False)),
                ('ste_date', models.DateField()),
                ('ste_lat_ship', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('ste_lon_ship', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('ste_depth_ship', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('ste_lat_mcal', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('ste_lon_mcal', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('ste_depth_mcal', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('ste_team', models.CharField(blank=True, max_length=50, null=True)),
                ('ste_instrument_cond', models.CharField(blank=True, max_length=4000, null=True)),
                ('ste_weather_cond', models.CharField(blank=True, max_length=4000, null=True)),
                ('ste_logs', models.CharField(blank=True, max_length=4000, null=True)),
                ('ste_notes', models.CharField(blank=True, max_length=4000, null=True)),
                ('crs', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.CrsCruises')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.DepDeployments')),
                ('set_type', models.ForeignKey(db_column='set_type', on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.SetStationEventCode')),
            ],
        ),
        migrations.CreateModel(
            name='RstRecordingStage',
            fields=[
                ('rst_id', models.AutoField(primary_key=True, serialize=False)),
                ('rst_channel_no', models.BigIntegerField(blank=True, null=True)),
                ('rst_active', models.CharField(max_length=1)),
                ('rst_duration', models.BigIntegerField()),
                ('rst_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('rst_gain', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('rsc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.RscRecordingSchedules')),
            ],
        ),
        migrations.CreateModel(
            name='RecRecordingEvents',
            fields=[
                ('rec_id', models.AutoField(primary_key=True, serialize=False)),
                ('rec_date_of_system_chk', models.DateField(blank=True, null=True)),
                ('rec_date_first_recording', models.DateField(blank=True, null=True)),
                ('rec_date_last_recording', models.DateField(blank=True, null=True)),
                ('rec_total_memory_used', models.BigIntegerField(blank=True, null=True)),
                ('rec_hf_mem', models.BigIntegerField(blank=True, null=True)),
                ('rec_lf_mem', models.BigIntegerField(blank=True, null=True)),
                ('rec_date_data_download', models.DateField(blank=True, null=True)),
                ('rec_data_store_url', models.CharField(blank=True, max_length=255, null=True)),
                ('rec_date_data_backed_up', models.DateField(blank=True, null=True)),
                ('rec_data_backup_url', models.CharField(blank=True, max_length=255, null=True)),
                ('rec_channel_count', models.BigIntegerField(blank=True, null=True)),
                ('rec_notes', models.CharField(blank=True, max_length=4000, null=True)),
                ('rec_first_in_water', models.DateField(blank=True, null=True)),
                ('rec_last_in_water', models.DateField(blank=True, null=True)),
                ('rsc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.RscRecordingSchedules')),
                ('rtt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.RttTimezoneCode')),
                ('tea_id_backed_up_by', models.ForeignKey(blank=True, db_column='tea_id_backed_up_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tea_id_backed_up_by', to='whalesdb.TeaTeamMembers')),
                ('tea_id_checked_by', models.ForeignKey(blank=True, db_column='tea_id_checked_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tea_id_checked_by', to='whalesdb.TeaTeamMembers')),
                ('tea_id_downloaded_by', models.ForeignKey(blank=True, db_column='tea_id_downloaded_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tea_id_downloaded_by', to='whalesdb.TeaTeamMembers')),
                ('tea_id_setup_by', models.ForeignKey(blank=True, db_column='tea_id_setup_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tea_id_setup_by', to='whalesdb.TeaTeamMembers')),
            ],
        ),
        migrations.CreateModel(
            name='EqpEquipment',
            fields=[
                ('eqp_id', models.AutoField(primary_key=True, serialize=False)),
                ('eqp_serial', models.CharField(max_length=50)),
                ('eqp_asset_id', models.CharField(max_length=50, unique=True)),
                ('eqp_date_purchase', models.DateField()),
                ('eqp_notes', models.CharField(blank=True, max_length=4000, null=True)),
                ('emm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EmmMakeModel')),
            ],
        ),
        migrations.AddField(
            model_name='emmmakemodel',
            name='eqt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EqtEquipmentTypeCode'),
        ),
        migrations.CreateModel(
            name='EdaEquipmentAttachments',
            fields=[
                ('eda_id', models.AutoField(primary_key=True, serialize=False)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.DepDeployments')),
                ('eqp', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EqpEquipment')),
                ('rec', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.RecRecordingEvents')),
            ],
        ),
        migrations.CreateModel(
            name='EccCalibrationValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecc_frequency', models.DecimalField(decimal_places=6, max_digits=10)),
                ('ecc_sensitivity', models.DecimalField(decimal_places=6, max_digits=10)),
                ('eca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EcaCalibrationEvent')),
            ],
        ),
        migrations.AddField(
            model_name='ecacalibrationevent',
            name='eca_attachement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='eca_attachement', to='whalesdb.EqpEquipment'),
        ),
        migrations.AddField(
            model_name='ecacalibrationevent',
            name='eca_hydrophone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='eca_hydrophone', to='whalesdb.EqpEquipment'),
        ),
        migrations.AddField(
            model_name='depdeployments',
            name='mor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.MorMooringSetups'),
        ),
        migrations.AddField(
            model_name='depdeployments',
            name='prj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.PrjProjects'),
        ),
        migrations.AddField(
            model_name='depdeployments',
            name='stn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.StnStations'),
        ),
        migrations.CreateModel(
            name='EprEquipmentParameters',
            fields=[
                ('epr_id', models.AutoField(primary_key=True, serialize=False)),
                ('emm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EmmMakeModel')),
                ('prm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.PrmParameterCode')),
            ],
            options={
                'unique_together': {('emm', 'prm')},
            },
        ),
        migrations.CreateModel(
            name='EhaHydrophoneAttachements',
            fields=[
                ('eha_id', models.AutoField(primary_key=True, serialize=False)),
                ('eda', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EdaEquipmentAttachments')),
                ('eqp', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EqpEquipment')),
            ],
            options={
                'unique_together': {('eda', 'eqp')},
            },
        ),
        migrations.CreateModel(
            name='EcpChannelProperties',
            fields=[
                ('ecp_id', models.AutoField(primary_key=True, serialize=False)),
                ('ecp_channel_no', models.BigIntegerField()),
                ('ecp_voltage_range_min', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ecp_voltage_range_max', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ecp_gain', models.BigIntegerField(blank=True, null=True)),
                ('emm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EmmMakeModel')),
                ('eqa_adc_bits', models.ForeignKey(db_column='eqa_adc_bits', on_delete=django.db.models.deletion.DO_NOTHING, to='whalesdb.EqaAdcBitsCode')),
            ],
            options={
                'unique_together': {('ecp_channel_no', 'emm')},
            },
        ),
    ]
