# Generated by Django 3.2.9 on 2021-11-29 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clicks', '0009_rename_image_image_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clicks.location'),
        ),
    ]