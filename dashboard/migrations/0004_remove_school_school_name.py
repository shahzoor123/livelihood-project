# Generated by Django 4.0.2 on 2022-03-13 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_district_school_id_remove_district_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='school_name',
        ),
    ]
