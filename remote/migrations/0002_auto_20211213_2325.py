# Generated by Django 3.2.9 on 2021-12-13 23:25

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remote',
            name='box',
        ),
        migrations.AddField(
            model_name='remote',
            name='singlebody',
            field=wagtail.core.fields.StreamField([('SingleBox', wagtail.core.blocks.StructBlock([('single', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(Required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]