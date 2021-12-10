# Generated by Django 3.2.9 on 2021-12-10 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0005_donation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='receipt',
            new_name='receipt_url',
        ),
        migrations.AddField(
            model_name='donation',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
