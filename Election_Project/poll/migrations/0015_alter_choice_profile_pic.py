# Generated by Django 4.0.4 on 2022-08-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0014_remove_choice_candidate_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to='images/static/images'),
        ),
    ]