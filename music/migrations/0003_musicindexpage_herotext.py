# Generated by Django 3.2.9 on 2021-12-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_musicindexpage_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicindexpage',
            name='herotext',
            field=models.TextField(max_length=250, null=True),
        ),
    ]