# Generated by Django 4.1.1 on 2023-01-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_alter_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_code',
            field=models.CharField(max_length=15),
        ),
    ]
