# Generated by Django 3.2.9 on 2021-12-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_alter_about_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='heading',
            field=models.TextField(max_length=250, null=True),
        ),
    ]