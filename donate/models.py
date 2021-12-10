from django.db import models

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from newpark.streams import blocks

class Donation(models.Model):
    """ Model to store donations made via Stripe"""
    donation_id = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(null=True, editable=False)
    status = models.CharField(max_length=32, null=False, editable=False)
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    customer_email = models.EmailField(max_length=254, null=False, blank=False)
    donation_amount = models.DecimalField(max_digits=6,
                                        decimal_places=0, null=False,
                                        default=0)
    receipt_url = models.URLField(max_length=200, null=False, blank=False, editable=False)


class DonateIndexPage(Page):
    """ Donation Page Index for Stripe Element """
    background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    color = ColorField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)

    box = RichTextField(blank=True, null=True)

    #CMS Content Panels
    content_panels = Page.content_panels + [
        ImageChooserPanel('cover', heading='Cover Image',),
        ImageChooserPanel('background', heading='Background Image',),
        NativeColorPanel('color', heading='Color Accent'),
        FieldPanel('body', heading='Support Us Content', classname='full'),
        FieldPanel('box', heading='Box',),
    ]
