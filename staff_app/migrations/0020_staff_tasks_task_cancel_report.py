# Generated by Django 4.2.1 on 2023-06-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0019_staff_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_tasks',
            name='task_cancel_report',
            field=models.TextField(default='', null=True),
        ),
    ]
