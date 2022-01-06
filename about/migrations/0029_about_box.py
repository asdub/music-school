# Generated by Django 3.2.9 on 2021-12-29 15:31

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0028_alter_about_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='box',
            field=wagtail.core.fields.StreamField([('NavBox', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('color', wagtail_color_panel.blocks.NativeColorBlock(default='#072660')), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]