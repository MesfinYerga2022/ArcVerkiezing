# Generated by Django 4.0.4 on 2022-08-09 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0013_remove_poll_candidate_count_choice_candidate_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='candidate_count',
        ),
    ]