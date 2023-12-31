# Generated by Django 4.2.7 on 2023-11-28 00:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0018_alter_car_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='picture',
            field=models.ImageField(default=None, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
