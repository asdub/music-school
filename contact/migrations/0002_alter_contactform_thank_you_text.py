# Generated by Django 3.2.9 on 2021-11-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='thank_you_text',
            field=models.CharField(max_length=250, null=True),
        ),
    ]