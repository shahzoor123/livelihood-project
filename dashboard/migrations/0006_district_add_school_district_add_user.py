# Generated by Django 4.0.2 on 2022-03-13 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_school_add_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='add_school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.school'),
        ),
        migrations.AddField(
            model_name='district',
            name='add_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.user'),
        ),
    ]
