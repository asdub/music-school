from django.db import models

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from newpark.streams import blocks
from . import services


class Remote(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading = RichTextField(blank=True, null=True)
    enable_hero = models.BooleanField(default=False)
    hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    herotext = models.TextField(max_length=250, blank=True, null=True)

    singlebody = StreamField(
        [
            ('SingleBox', blocks.SingleBlock()),
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('singlebody'),
        index.SearchField('heading'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('heading', heading='Heading Blurb'),
        ImageChooserPanel('cover', heading='Cover Image',),
        FieldRowPanel([
            ImageChooserPanel('hero', help_text='Hero Image', classname="col12"),
            FieldPanel('herotext', classname="col12"),
            FieldPanel('enable_hero', help_text="Select to enable hero banner", classname="col4"),
        ], heading="Hero Settings"),
        StreamFieldPanel('singlebody', heading='Single Item Content',),
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['zoom_users'] = services.get_users()
        return context