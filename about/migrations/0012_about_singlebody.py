# Generated by Django 3.2.9 on 2021-12-03 16:03

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_alter_about_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='singlebody',
            field=wagtail.core.fields.StreamField([('SingleBox', wagtail.core.blocks.StructBlock([('single', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(Required=False))])))]))], blank=True, null=True),
        ),
    ]
