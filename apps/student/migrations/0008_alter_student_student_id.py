# Generated by Django 4.1.1 on 2022-12-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
