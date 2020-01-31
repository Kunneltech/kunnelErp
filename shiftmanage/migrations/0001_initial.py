# Generated by Django 3.0.2 on 2020-01-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shiftInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shiftstart', models.TimeField()),
                ('shiftend', models.TimeField()),
                ('break1start', models.TimeField()),
                ('break1end', models.TimeField()),
                ('lunchbreakstart', models.TimeField()),
                ('lunchbreakend', models.TimeField()),
                ('break2start', models.TimeField()),
                ('break2end', models.TimeField()),
            ],
        ),
    ]