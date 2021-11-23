from django.db import models
from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class MyCustomSettings(BaseSetting):
    contact_form = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL)

    panels = [
        # note the page type declared within the pagechooserpanel
        PageChooserPanel('contact_form', ['contact.ContactForm']),
    ]


class HomePage(Page):
    #About Section
    about_cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    about_heading = models.CharField(max_length=250, null=True)
    about_body = RichTextField(blank=True, null=True)
    about_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='About Button Link'
    )

    #Music Section
    music_cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    music_heading = models.CharField(max_length=250, null=True)
    music_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Music Button Link'
    )

    #Contact Section
    contact_phone = models.CharField(max_length=100, null=True)
    contact_email = models.CharField(max_length=100, null=True)
    contact_address = RichTextField(blank=True, null=True)
    googlemaps_embed = models.CharField(max_length=350, null=True)

    # Search
    search_fields = Page.search_fields + [
        index.SearchField('about_heading'),
        index.SearchField('about_body'),
    ]

    #CMS Content Panels
    content_panels = Page.content_panels + [
        ImageChooserPanel('about_cover', heading='About Cover Image',),
        FieldPanel('about_heading', heading='About Section Heading',),
        FieldPanel('about_body', heading='About Content', classname='full'),
        PageChooserPanel('about_page'),
        ImageChooserPanel('music_cover', heading='Music Cover Image',),
        FieldPanel('music_heading', heading='Music Section Heading',),
        PageChooserPanel('music_page'),
        FieldPanel('contact_phone', heading='Contact Number'),
        FieldPanel('contact_email', heading='Contact Email'),
        FieldPanel('contact_address', heading='Contact Address'),
        FieldPanel('googlemaps_embed', heading='Google Maps Embed Link')
    ]



