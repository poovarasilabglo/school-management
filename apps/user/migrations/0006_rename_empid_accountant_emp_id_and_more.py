# Generated by Django 4.1.1 on 2022-12-21 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountant',
            old_name='empId',
            new_name='emp_id',
        ),
        migrations.RenameField(
            model_name='accountant',
            old_name='isAccountant',
            new_name='is_accountant',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='empId',
            new_name='emp_id',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='isTeacher',
            new_name='is_teacher',
        ),
    ]
