# Generated by Django 3.1.3 on 2021-01-22 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210122_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='file',
            new_name='file_upload',
        ),
    ]
