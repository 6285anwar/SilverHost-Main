# Generated by Django 4.2.1 on 2023-06-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0020_staff_tasks_task_cancel_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_tasks',
            name='task_cancel_report',
            field=models.TextField(null=True),
        ),
    ]
