# Generated by Django 3.2.9 on 2021-11-28 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clicks', '0008_auto_20211128_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='photo',
        ),
    ]