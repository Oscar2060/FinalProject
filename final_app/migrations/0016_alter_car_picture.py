# Generated by Django 4.2.7 on 2023-11-27 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0015_car_picture_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='picture',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]