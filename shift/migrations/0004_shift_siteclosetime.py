# Generated by Django 3.0.2 on 2020-02-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0003_auto_20200213_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='siteclosetime',
            field=models.TimeField(default='00:00:00'),
            preserve_default=False,
        ),
    ]
