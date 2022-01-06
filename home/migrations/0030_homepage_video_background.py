# Generated by Django 3.2.9 on 2021-12-28 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0029_auto_20211220_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_background',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
