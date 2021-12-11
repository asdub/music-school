from django.db import models
from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_icon_picker.fields import IconField
from wagtail_icon_picker.edit_handlers import FontAwesomeIconPickerPanel

import datetime

class WorkshopsIndexPage(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    box1_icon = IconField(blank=True, null=True)
    box1 = RichTextField(blank=True, null=True)
    box2_icon = IconField(blank=True, null=True)
    box2 =  RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover', heading="Cover Image"),
        FontAwesomeIconPickerPanel('box1_icon', heading="Box 1 Icon"),
        FieldPanel('box1', classname="full", heading="Box 1 Content"),
        FontAwesomeIconPickerPanel('box2_icon', heading="Box 2 Icon"),
        FieldPanel('box2', classname="full", heading="Box 2 Content"),
    ]
    

class WorkshopsPost(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    subheading = models.TextField(max_length=250, null=True)
    date = models.DateField("Workshop Date")
    start_time = models.TimeField("Start Time", default=datetime.time(19, 00))
    end_time = models.TimeField("End Time", default=datetime.time(21, 00))
    link_url = models.URLField(null=True)
    price = models.DecimalField(max_digits=6,
                            decimal_places=2, null=True,
                            default=0)
    body = RichTextField(blank=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('subheading', heading="Heading Text"),
        ImageChooserPanel('cover'),
        FieldRowPanel([
            FieldPanel('date', classname="col6"),
            FieldPanel('price', classname="col6"),
            FieldPanel('start_time', classname="col6"),
            FieldPanel('end_time', classname="col6"),
        ], heading="Workshop Details"),
        FieldPanel('body', classname="full"),
        FieldPanel('link_url', heading="External URL"),
    ]