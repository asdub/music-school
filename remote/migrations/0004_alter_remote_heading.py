# Generated by Django 3.2.9 on 2021-12-13 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0003_rename_body_remote_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remote',
            name='heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]
