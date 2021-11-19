from django.db import models
from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel


class HomePage(Page):
    aboutcover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    aboutheading = models.CharField(max_length=250, null=True)
    aboutbody = RichTextField(blank=True)
    about_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    search_fields = Page.search_fields + [
        index.SearchField('aboutheading'),
        index.SearchField('aboutbody'),
    ]

    content_panels = [
        FieldPanel('title'),
        ImageChooserPanel('aboutcover', heading='Cover Image',),
        FieldPanel('aboutheading', heading='Section Heading',),
        FieldPanel('aboutbody', classname="full"),
        PageChooserPanel('about_page'),
    ]
