# Generated by Django 3.2.9 on 2021-11-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicks', '0014_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]