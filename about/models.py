from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.search import index
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from newpark.streams import blocks


class AboutIndexPage(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
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
        ImageChooserPanel('cover', heading='Cover Image',),
        FieldPanel('body', heading='About Blurb'),
        StreamFieldPanel('box', heading='Navigation Boxes',),
    ]

class About(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    color = ColorField(blank=True, null=True)
    heading = models.TextField(max_length=250, null=True)
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
        StreamFieldPanel('body', heading='List Content',),
        StreamFieldPanel('singlebody', heading='Single Item Content',),
    ]
