# Generated by Django 3.2.4 on 2021-12-05 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20211205_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='present',
            new_name='is_present',
        ),
    ]
