# Generated by Django 4.2.7 on 2023-11-26 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0005_remove_car_owner_alter_userprofile_cars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='cars',
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='final_app.userprofile'),
        ),
    ]
