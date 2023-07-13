# Generated by Django 4.2.1 on 2023-06-07 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0015_alter_staff_tasks_task_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Project_Task_Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(default='0', max_length=255)),
                ('report_date', models.DateField()),
                ('which_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff_app.staff_registration')),
                ('which_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff_app.staff_tasks')),
            ],
        ),
    ]