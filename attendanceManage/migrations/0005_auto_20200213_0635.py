# Generated by Django 3.0.2 on 2020-02-13 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManage', '0004_auto_20200212_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancemanage',
            name='numberofhours',
        ),
        migrations.RemoveField(
            model_name='attendancemanage',
            name='overtimeallocated',
        ),
        migrations.RemoveField(
            model_name='attendancemanage',
            name='overtimeworked',
        ),
    ]