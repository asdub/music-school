# Generated by Django 3.2.9 on 2021-12-12 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_music_buttons_enabled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='button_a_page',
            new_name='button_a',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='button_a_page_text',
            new_name='button_a_text',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='button_b_page',
            new_name='button_b',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='button_b_page_text',
            new_name='button_b_text',
        ),
    ]
