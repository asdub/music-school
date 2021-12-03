# Generated by Django 3.2.9 on 2021-12-03 12:31

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_aboutindexpage_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='color',
            field=wagtail_color_panel.fields.ColorField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='body',
            field=wagtail.core.fields.StreamField([('ListBox', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000')), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]
