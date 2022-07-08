# Generated by Django 4.0.4 on 2022-07-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_rename_question_choice_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='candidate',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AddField(
            model_name='poll',
            name='candidate_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='candidate_three',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='poll',
            name='candidate_two',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
