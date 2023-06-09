# Generated by Django 4.1.3 on 2023-06-14 19:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instabam', '0015_followerscount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followerscount',
            name='from_userprofile',
        ),
        migrations.RemoveField(
            model_name='followerscount',
            name='to_userprofile',
        ),
        migrations.AddField(
            model_name='followerscount',
            name='follower',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='followerscount',
            name='user',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
