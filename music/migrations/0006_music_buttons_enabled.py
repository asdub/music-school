# Generated by Django 3.2.9 on 2021-12-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20211212_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='buttons_enabled',
            field=models.BooleanField(default=False),
        ),
    ]