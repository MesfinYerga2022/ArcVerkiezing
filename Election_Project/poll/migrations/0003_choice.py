# Generated by Django 4.0.4 on 2022-06-28 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_poll_close_date_poll_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('description_text', models.CharField(default='', max_length=2000)),
                ('candidate_image', models.ImageField(default='', upload_to='Images')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.poll')),
            ],
        ),
    ]
