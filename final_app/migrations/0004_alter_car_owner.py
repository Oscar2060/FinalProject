# Generated by Django 4.2.7 on 2023-11-26 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0003_userprofile_alter_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.userprofile'),
        ),
    ]
