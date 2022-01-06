# Generated by Django 3.2.9 on 2021-12-12 15:49

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('box', wagtail.core.fields.StreamField([('NavBox', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000')), ('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])))]))], blank=True, null=True)),
                ('cover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MusicGrid',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('color', wagtail_color_panel.fields.ColorField(blank=True, max_length=7, null=True)),
                ('heading', models.TextField(max_length=250, null=True)),
                ('box', wagtail.core.fields.StreamField([('SingleBox', wagtail.core.blocks.StructBlock([('single', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(Required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))]))], blank=True, null=True)),
                ('cover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('color', wagtail_color_panel.fields.ColorField(blank=True, max_length=7, null=True)),
                ('heading', models.TextField(max_length=250, null=True)),
                ('body', wagtail.core.fields.StreamField([('ListBox', wagtail.core.blocks.StructBlock([('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=False))]))), ('single_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_gallery', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('gallery_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])))])))]))], blank=True, null=True)),
                ('singlebody', wagtail.core.fields.StreamField([('SingleBox', wagtail.core.blocks.StructBlock([('single', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('cover', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('subtext', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(Required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))]))], blank=True, null=True)),
                ('cover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
