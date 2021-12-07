# Generated by Django 3.2.9 on 2021-12-07 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0017_auto_20211202_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='events_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]