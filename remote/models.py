from django.db import models

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from newpark.streams import blocks
from . import services


class RemoteIndexPage(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    enable_hero = models.BooleanField(default=False)
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

    content_panels = Page.content_panels + [
        FieldPanel('body', heading='Heading Blurb'),
        ImageChooserPanel('cover', heading='Cover Image',),
        FieldRowPanel([
            ImageChooserPanel('hero', help_text='Hero Image', classname="col12"),
            FieldPanel('herotext', classname="col12"),
            FieldPanel('enable_hero', help_text="Select to enable hero banner", classname="col4"),
        ], heading="Hero Settings"),
        StreamFieldPanel('box', heading='Navigation Boxes',),
    ]

class Video(models.Model):
    """ Create Zoom User object """
    id = models.CharField(primary_key=True, max_length=100)
    type = models.IntegerField(default=0, null=False)
    name = models.CharField(max_length=100)
    url = models.URLField()
    img = models.ImageField(upload_to='video_poster')


class RemoteVideo(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading =  RichTextField(blank=True, null=True)

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
        FieldPanel('heading', heading='Heading Blurb'),
        ImageChooserPanel('cover', heading='Cover Image',),
        StreamFieldPanel('singlebody', heading='Single Item Content',),
    ]


    def get_context(self, request, *args, **kwargs):
        # Add sorted Zoom user list to context
        context = super().get_context(request, *args, **kwargs)
        video_list = services.get_video()
        sorted_video_list = sorted(video_list, key=lambda l: (l.name))

        context['gateway1_video'] = sorted_video_list
        return context



class Remote(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading =  RichTextField(blank=True, null=True)

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
        FieldPanel('heading', heading='Heading Blurb'),
        ImageChooserPanel('cover', heading='Cover Image',),
        StreamFieldPanel('singlebody', heading='Single Item Content',),
    ]


    def get_context(self, request, *args, **kwargs):
        # Add sorted Zoom user list to context
        context = super().get_context(request, *args, **kwargs)
        user_list = services.get_users()
        sorted_user_list = sorted(user_list, key=lambda l: (l.lname))

        context['zoom_users'] = sorted_user_list
        return context