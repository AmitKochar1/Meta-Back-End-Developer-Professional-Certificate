# Generated by Django 5.0 on 2024-01-07 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_rename_cuisine_menu_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='itemname',
        ),
    ]
