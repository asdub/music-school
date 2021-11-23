# Generated by Django 3.2.9 on 2021-11-23 11:58

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211123_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='id',
        ),
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='custom_form_fields', serialize=False, to='home.homepage'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]