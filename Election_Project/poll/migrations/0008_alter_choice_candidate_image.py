# Generated by Django 4.0.4 on 2022-07-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0007_alter_choice_candidate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='candidate_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='static/images'),
        ),
    ]