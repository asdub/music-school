# Generated by Django 3.2.9 on 2021-12-06 21:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0016_auto_20211206_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=wagtail.core.fields.StreamField([('ListBox', wagtail.core.blocks.StructBlock([('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=False))]))), ('single_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_gallery', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('gallery_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])))])))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutindexpage',
            name='box',
            field=wagtail.core.fields.StreamField([('NavBox', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000')), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]
