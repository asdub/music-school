from django.db import models

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

    content_panels = [
        FieldPanel('title'),
        ImageChooserPanel('cover', heading='Cover Image',),
        FieldPanel('body', heading='Heading Blurb'),
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
    heading = models.TextField(blank=True, null=True)
    standard = StreamField(
        [
            ('StandardBox', blocks.StandardBlock()),
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

    table = StreamField(
        [
            ('TableBox', blocks.TableBlock()),
        ],
        null=True,
        blank=True,
    )

    buttons = StreamField(
        [
            ('Buttons', blocks.ButtonBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels =  Page.content_panels + [
        FieldPanel('heading', heading='Page Intro Text'),
        ImageChooserPanel('cover', heading='Cover Image',),
        NativeColorPanel('color', heading='Color Accent'),
        StreamFieldPanel('buttons', heading='Top Navigation Button Settings',),
        StreamFieldPanel('standard', heading='Standard Content',),
        StreamFieldPanel('body', heading='List Content',),
        StreamFieldPanel('singlebody', heading='Single Item Content',),
        StreamFieldPanel('table', heading='Table Content',),
    ]


class AboutLocationPage(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    color = ColorField(default='#fafafa', blank=True, null=True)
    heading = models.TextField(max_length=250, null=True)
    body = StreamField(
        [
            ('StandardBox', blocks.StandardBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels =  Page.content_panels + [
        FieldPanel('heading', heading='Page Intro Text'),
        ImageChooserPanel('cover', heading='Cover Image',),
        NativeColorPanel('color', heading='Color Accent'),
        StreamFieldPanel('body', heading='Standard Content',),
    ]



