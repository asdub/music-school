# Generated by Django 3.2.9 on 2021-12-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_musicindexpage_herotext'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicindexpage',
            name='enable_hero',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='musicindexpage',
            name='enable_pathway',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='musicindexpage',
            name='herotext',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
