# Generated by Django 4.1.3 on 2024-01-07 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinks',
            old_name='drink',
            new_name='drink_name',
        ),
    ]
