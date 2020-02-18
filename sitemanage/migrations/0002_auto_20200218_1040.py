# Generated by Django 3.0.2 on 2020-02-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitemanage',
            old_name='endBuffer',
            new_name='end_buffer',
        ),
        migrations.RenameField(
            model_name='sitemanage',
            old_name='endDate',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='sitemanage',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='sitemanage',
            old_name='lunchTime',
            new_name='lunch_time',
        ),
        migrations.RenameField(
            model_name='sitemanage',
            old_name='startTime',
            new_name='start_buffer',
        ),
        migrations.RenameField(
            model_name='sitemanage',
            old_name='startDate',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='sitemanage',
            old_name='strtBuffer',
            new_name='start_time',
        ),
        migrations.RemoveField(
            model_name='sitemanage',
            name='clientName',
        ),
        migrations.RemoveField(
            model_name='sitemanage',
            name='projectIncharge',
        ),
        migrations.RemoveField(
            model_name='sitemanage',
            name='salaryStructure',
        ),
        migrations.RemoveField(
            model_name='sitemanage',
            name='siteEngineer',
        ),
        migrations.RemoveField(
            model_name='sitemanage',
            name='siteid',
        ),
        migrations.RemoveField(
            model_name='sitemanage',
            name='typeOfProject',
        ),
        migrations.AddField(
            model_name='sitemanage',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='sitemanage',
            name='client_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='sitemanage',
            name='project_manager',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='sitemanage',
            name='project_type',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='sitemanage',
            name='salary_structure',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='sitemanage',
            name='site_engineer',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='sitemanage',
            name='site_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='sitemanage',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]