# Generated by Django 4.1.1 on 2023-01-03 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_alter_teacher_teacher_id'),
        ('student', '0011_attendance_absent_attendance_half_leaverequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]
