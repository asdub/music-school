# Generated by Django 3.2.9 on 2021-12-12 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('music', '0004_auto_20211212_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='button_a_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button A Page'),
        ),
        migrations.AddField(
            model_name='music',
            name='button_a_page_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='button_a_url',
            field=models.URLField(blank=True, max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='button_b_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button B Page'),
        ),
        migrations.AddField(
            model_name='music',
            name='button_b_page_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='button_b_url',
            field=models.URLField(blank=True, max_length=232, null=True),
        ),
    ]
