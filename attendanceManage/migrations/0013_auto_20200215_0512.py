# Generated by Django 3.0.2 on 2020-02-15 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManage', '0012_auto_20200214_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labourworktime',
            name='labourerid',
            field=models.CharField(max_length=50),
        ),
    ]