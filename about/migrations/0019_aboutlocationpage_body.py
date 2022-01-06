# Generated by Django 3.2.9 on 2021-12-06 22:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0018_aboutlocationpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutlocationpage',
            name='body',
            field=wagtail.core.fields.StreamField([('ListBox', wagtail.core.blocks.StructBlock([('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=False))]))), ('single_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_gallery', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('gallery_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])))])))]))], blank=True, null=True),
        ),
    ]
