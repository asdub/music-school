# Generated by Django 3.2.9 on 2021-12-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_auto_20211130_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribeform',
            name='list_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
