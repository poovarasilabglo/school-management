# Generated by Django 4.1.1 on 2022-12-31 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_alter_teacher_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
