# Generated by Django 4.2.1 on 2023-06-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0024_alter_attendance_day_break_total_break_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='today_total_break_time',
            field=models.CharField(default='00:00:00', max_length=200),
        ),
    ]
