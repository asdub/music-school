# Generated by Django 3.2.9 on 2021-12-18 15:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0024_about_standard'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='table',
            field=wagtail.core.fields.StreamField([('TableBox', wagtail.core.blocks.StructBlock([('table', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('titles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=False))], block_counts={'text': {'max_num': 4}}))), ('rows', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('course', wagtail.core.blocks.CharBlock(required=False)), ('class_lenght', wagtail.core.blocks.CharBlock(required=False)), ('duration', wagtail.core.blocks.CharBlock(required=False)), ('price', wagtail.core.blocks.CharBlock(required=False))])))], block_counts={'titles': {'max_mun': 1}})))]))], blank=True, null=True),
        ),
    ]
