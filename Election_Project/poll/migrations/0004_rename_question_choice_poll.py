# Generated by Django 4.0.4 on 2022-07-05 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='poll',
        ),
    ]
