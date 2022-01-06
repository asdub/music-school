# Generated by Django 3.2.9 on 2021-12-17 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0019_alter_sitesettings_events_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='festival_button',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='festival_cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='festival_heading',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='festival_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Support Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='workshops_button',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='workshops_cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='workshops_heading',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='workshops_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Support Button Link'),
        ),
    ]
