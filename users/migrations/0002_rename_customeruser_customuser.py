# Generated by Django 5.1.5 on 2025-02-01 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerUser',
            new_name='CustomUser',
        ),
    ]
