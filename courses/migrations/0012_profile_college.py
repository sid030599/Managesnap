# Generated by Django 4.0.1 on 2022-06-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_mycourses_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.CharField(default='abc college', max_length=100),
        ),
    ]
