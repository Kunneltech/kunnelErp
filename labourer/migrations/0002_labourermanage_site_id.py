# Generated by Django 3.0.2 on 2020-02-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labourer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourermanage',
            name='site_id',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
