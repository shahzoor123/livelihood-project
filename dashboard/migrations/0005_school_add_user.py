# Generated by Django 4.0.2 on 2022-03-13 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_school_school_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='add_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.user'),
        ),
    ]
