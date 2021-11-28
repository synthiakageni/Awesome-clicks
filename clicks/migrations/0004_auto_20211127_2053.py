# Generated by Django 3.2.9 on 2021-11-27 17:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clicks', '0003_remove_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['date_posted']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['location']},
        ),
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clicks.location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]