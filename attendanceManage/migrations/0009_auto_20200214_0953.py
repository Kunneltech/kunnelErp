# Generated by Django 3.0.2 on 2020-02-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManage', '0008_auto_20200214_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labourworktime',
            name='intime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='labourworktime',
            name='otEnd',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='labourworktime',
            name='otStart',
            field=models.TimeField(null=True),
        ),
    ]