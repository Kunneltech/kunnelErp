# Generated by Django 3.0.2 on 2020-02-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManage', '0002_lbourworktime'),
    ]

    operations = [
        migrations.AddField(
            model_name='lbourworktime',
            name='labourerid',
            field=models.CharField(default=1234567, max_length=50),
            preserve_default=False,
        ),
    ]
