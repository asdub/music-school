from django.db import models
from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

class AboutIndexPage(Page):
    pass

class About(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('heading'),
        index.SearchField('body'),
    ]

    content_panels = [
        FieldPanel('title'),
        ImageChooserPanel('cover', heading='Cover Image',),
        FieldPanel('heading', heading='Section Heading',),
        FieldPanel('body', classname="full"),
    ]