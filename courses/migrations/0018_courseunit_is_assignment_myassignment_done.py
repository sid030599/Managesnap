# Generated by Django 4.0.1 on 2022-06-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_assignment_myassignment_grades_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseunit',
            name='is_assignment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myassignment',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
