# Generated by Django 3.2.9 on 2021-11-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicks', '0005_auto_20211127_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='location',
            name='location',
            field=models.CharField(default='1', editable=False, max_length=100),
        ),
    ]
