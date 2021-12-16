from django.db import models
from django.conf import settings

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
    type = models.CharField(max_length=100)
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
    video_source = models.IntegerField(choices=(
        (1, 'Gateway 1'), 
        (2, 'Gateway 2'),
        (3, 'Gateway P')
        ),
        default=1,
        null=False, 
        blank=False,
    )

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
        FieldPanel('video_source', heading='Video Source'),
        ImageChooserPanel('cover', heading='Cover Image',),
        StreamFieldPanel('singlebody', heading='Single Item Content',),
    ]


    def get_context(self, request, *args, **kwargs):
        # Add Gateway videos to contect
        context = super().get_context(request, self, *args, **kwargs)
        if self.video_source == 1:
            gateway = settings.GATEWAY1
        elif self.video_source == 2:
             gateway = settings.GATEWAY2
        else: 
             gateway = settings.GATEWAY3
        video_list = services.get_video(gateway)
        sorted_video_list = sorted(video_list, key=lambda l: (l.name))

        context['gateway_video'] = sorted_video_list
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