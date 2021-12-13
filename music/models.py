from django.db import models

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from newpark.streams import blocks


class MusicIndexPage(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    enable_hero = models.BooleanField(default=False)
    enable_pathway = models.BooleanField(default=False)
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    herotext = models.TextField(max_length=250, blank=True, null=True)
    body = RichTextField(blank=True, null=True)

    box = StreamField(
        [
            ('NavBox', blocks.NavBlock()),
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('box'),
        index.SearchField('body'),
    ]

    content_panels = [
        FieldPanel('title'),
        FieldPanel('body', heading='Heading Blurb'),
        ImageChooserPanel('cover', heading='Cover Image',),
        FieldRowPanel([
            ImageChooserPanel('hero', help_text='Hero Image', classname="col12"),
            FieldPanel('herotext', classname="col12"),
            FieldPanel('enable_hero', help_text="Select to enable hero banner", classname="col4"),
            FieldPanel('enable_pathway', help_text="Select to enable Newpark Pathways Map", classname="col4"),
        ], heading="Hero Settings"),
        StreamFieldPanel('box', heading='Navigation Boxes',),
    ]


class Music(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    color = ColorField(blank=True, null=True)
    heading = models.TextField(max_length=250, null=True)

    buttons = StreamField(
        [
            ('Buttons', blocks.ButtonBlock()),
        ],
        null=True,
        blank=True,
    )
   
    body = StreamField(
        [
            ('ListBox', blocks.ListBlock()),
        ],
        null=True,
        blank=True,
    )

    singlebody = StreamField(
        [
            ('SingleBox', blocks.SingleBlock()),
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('heading'),
        index.SearchField('body'),
        index.SearchField('singlebody'),
    ]

    content_panels =  Page.content_panels + [
        FieldPanel('heading', heading='Page Intro Text'),
        ImageChooserPanel('cover', heading='Cover Image',),
        NativeColorPanel('color', heading='Color Accent'),
        StreamFieldPanel('buttons', heading='Top Navigation Button Settings',),
        StreamFieldPanel('body', heading='Multi Item Content',),
        StreamFieldPanel('singlebody', heading='Single Item Content',),
    ]


class MusicGrid(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    color = ColorField(blank=True, null=True)
    heading = models.TextField(max_length=250, null=True)
    box = StreamField(
        [
            ('SingleBox', blocks.SingleBlock()),
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('heading'),
    ]

    content_panels =  Page.content_panels + [
        FieldPanel('heading', heading='Page Intro Text'),
        ImageChooserPanel('cover', heading='Cover Image',),
        NativeColorPanel('color', heading='Color Accent'),
        StreamFieldPanel('box', heading='Grid Box',),
    ]
