# Generated by Django 3.2.9 on 2021-12-15 19:06

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('remote', '0005_auto_20211215_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteVideo',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('heading', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('singlebody', wagtail.core.fields.StreamField([('SingleBox', wagtail.core.blocks.StructBlock([('single', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(Required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))]))], blank=True, null=True)),
                ('cover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
