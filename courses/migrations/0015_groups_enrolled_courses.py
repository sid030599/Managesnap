# Generated by Django 4.0.1 on 2022-06-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_groups_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='enrolled_courses',
            field=models.ManyToManyField(to='courses.course'),
        ),
    ]
