# Generated by Django 4.1.3 on 2023-05-27 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instabam', '0003_delete_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repost',
            old_name='tweet',
            new_name='post',
        ),
    ]
