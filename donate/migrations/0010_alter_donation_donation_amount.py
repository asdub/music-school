# Generated by Django 3.2.9 on 2021-12-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0009_auto_20211210_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_amount',
            field=models.CharField(default=0, editable=False, max_length=12),
        ),
    ]
