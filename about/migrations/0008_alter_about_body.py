# Generated by Django 3.2.9 on 2021-12-03 12:37

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_alter_about_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=wagtail.core.fields.StreamField([('ListBox', wagtail.core.blocks.StructBlock([('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('subtext', wagtail.core.blocks.TextBlock(required=True)), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(Required=True))])))])))]))], blank=True, null=True),
        ),
    ]
