# Generated by Django 4.2.1 on 2023-06-10 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0022_attendance_day_break'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_day_break',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff_app.staff_registration'),
        ),
    ]
