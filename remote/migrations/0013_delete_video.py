# Generated by Django 3.2.9 on 2021-12-19 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0012_alter_remotevideo_video_source'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
    ]