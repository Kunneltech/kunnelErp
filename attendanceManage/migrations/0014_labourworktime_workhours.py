# Generated by Django 3.0.2 on 2020-02-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManage', '0013_auto_20200215_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourworktime',
            name='workhours',
            field=models.TimeField(null=True),
        ),
    ]
