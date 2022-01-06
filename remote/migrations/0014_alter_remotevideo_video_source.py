# Generated by Django 3.2.9 on 2021-12-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0013_delete_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotevideo',
            name='video_source',
            field=models.IntegerField(blank=True, choices=[(1, 'Gateway 1'), (2, 'Gateway 2'), (3, 'Gateway P'), (4, 'Pro Tip Videos')], default=1, null=True),
        ),
    ]