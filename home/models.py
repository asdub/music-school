from django.db import models
from django.conf import settings

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import ( 
    FieldPanel,
    PageChooserPanel, 
    MultiFieldPanel,
    FieldRowPanel,
)
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from wagtailseo.models import SeoMixin

from newpark.streams import blocks
from remote import services

@register_setting
class MyCustomSettings(BaseSetting):
    contact_form = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL)

    panels = [
        # note the page type declared within the pagechooserpanel
        PageChooserPanel('contact_form', ['contact.ContactForm']),
    ]

@register_setting
class SubscribeSettings(BaseSetting):
    subscribe_form = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL)

    panels = [
        # note the page type declared within the pagechooserpanel
        PageChooserPanel('subscribe_form', ['subscribe.SubscribeForm']),
    ]

@register_setting
class SiteSettings(BaseSetting):
    #Site Logo
    logo = models.OneToOneField(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Site logo')

    #Contact Section
    contact_phone = models.CharField(max_length=100, null=True)
    contact_email = models.CharField(max_length=100, null=True)
    contact_address = RichTextField(blank=True, null=True)
    googlemaps_embed = models.CharField(max_length=350, null=True)
    events_image = models.OneToOneField(
        Image, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
         related_name='+', 
         verbose_name='Event Image'
    )

    #Social Media
    facebook =  models.URLField(max_length=200, null=True)
    instagram =  models.URLField(max_length=200, null=True)
    twitter = models.URLField(max_length=200, null=True)
    spotify = models.URLField(max_length=200, null=True)

    #Privacy
    privacy= models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Privacy Policy'
    )

    
    panels = [
        MultiFieldPanel([
            ImageChooserPanel('logo', heading="Site Logo"),
            FieldRowPanel([
                FieldPanel('contact_phone', heading='Contact Number'),
                FieldPanel('contact_email', heading='Contact Email'),
            ], classname='col12'),
            FieldPanel('contact_address', heading='Contact Address'),
            FieldPanel('googlemaps_embed', heading='Google Maps Embed Link'),
            ImageChooserPanel('events_image', heading="Events Page Image"),
        ], heading="Contact Information"),
    ] + [ 
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('facebook', heading='Facebook URL'),
                FieldPanel('instagram', heading='Instagram URL'),
            ], classname='col12'),
            FieldRowPanel([
                FieldPanel('twitter', heading='Twitter URL'),
                FieldPanel('spotify', heading='Spotify URL'),
            ], classname='col12'),
        ], heading="Social Media"),
    ] + [ 
        MultiFieldPanel([
            FieldRowPanel([
                PageChooserPanel('privacy')
            ], classname='col12'),
        ], heading="Privacy Policy"),
    ]
class HomePage(SeoMixin, Page):
    #Video Section
    video_cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    video_heading = models.CharField(max_length=250, null=True)
    video_body = RichTextField(blank=True, null=True)
    video_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Video Button Link'
    )
    video_button = models.CharField(max_length=100, null=True)

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
        verbose_name='Button Link'
    )
    about_button = models.CharField(max_length=100, null=True)

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
        verbose_name='Button Link'
    )
    music_button = models.CharField(max_length=100, null=True)


    #Suppot Section
    support_cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    support_heading = models.CharField(max_length=250, null=True)
    support_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    support_button = models.CharField(max_length=100, null=True)

    #Festival Seciton
    festival_cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    festival_heading = models.CharField(max_length=250, null=True)
    festival_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    festival_button = models.CharField(max_length=100, null=True)

    #Workshops Seciton
    workshops_cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    workshops_heading = models.CharField(max_length=250, null=True)
    workshops_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    workshops_button = models.CharField(max_length=100, null=True)

    # Pathways 
    pathway1 = models.CharField(max_length=100, null=True)
    pathway1_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    pathway2 = models.CharField(max_length=100, null=True)
    pathway2_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    pathway3 = models.CharField(max_length=100, null=True)
    pathway3_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    pathway4 = models.CharField(max_length=100, null=True)
    pathway4_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    pathway5 = models.CharField(max_length=100, null=True)
    pathway5_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    pathway6 = models.CharField(max_length=100, null=True)
    pathway6_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    pathway7 = models.CharField(max_length=100, null=True)
    pathway7_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    pathway8 = models.CharField(max_length=100, null=True)
    pathway8_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )
    pathway9 = models.CharField(max_length=100, null=True)
    pathway9_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Button Link'
    )

    # Content Panels
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('video_cover', heading='Video Poster',),
            FieldPanel('video_heading', heading='Video Section Heading',),
            FieldPanel('video_body', heading='Video Content'),
            PageChooserPanel('video_page'),
            FieldPanel('video_button', heading='Video Button Text'),
        ], heading="Home - Hero Video"),
        MultiFieldPanel([
            ImageChooserPanel('about_cover', heading='Cover Image',),
            FieldPanel('about_heading', heading='Section Heading',),
            FieldPanel('about_body', heading='Content'),
            PageChooserPanel('about_page'),
            FieldPanel('about_button', heading='Button Text'),
        ], heading="Home - About Section"),
        MultiFieldPanel([
            ImageChooserPanel('music_cover', heading='Cover Image',),
            FieldPanel('music_heading', heading='Section Heading',),
            PageChooserPanel('music_page'),
            FieldPanel('music_button', heading='Button Text'),
        ], heading="Home - Music Section"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('pathway1', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway1_page'),
            ], classname="col6"),
            FieldRowPanel([
                FieldPanel('pathway2', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway2_page'),
            ], classname="col6"),
            FieldRowPanel([
                FieldPanel('pathway3', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway3_page'),
            ], classname="col6"),
            FieldRowPanel([
                FieldPanel('pathway4', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway4_page'),
            ], classname="col6"),
            FieldRowPanel([
                FieldPanel('pathway5', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway5_page'),
            ], classname="col6"),
            FieldRowPanel([
                FieldPanel('pathway6', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway6_page'),
            ], classname="col6"),
            FieldRowPanel([
                FieldPanel('pathway7', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway7_page'),
            ], classname="col6"),
            FieldRowPanel([
                FieldPanel('pathway8', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway8_page'),
            ], classname="col6"),
            FieldRowPanel([
                FieldPanel('pathway9', heading='Button Text', classname="col12 btn"),
                PageChooserPanel('pathway9_page'),
            ], classname="col6"),
        ], heading="Home - Music Pathways"),
        MultiFieldPanel([
            ImageChooserPanel('festival_cover', heading='Festival Cover Image',),
            FieldPanel('festival_heading', heading='Festival Section Heading',),
            PageChooserPanel('festival_page'),
            FieldPanel('festival_button', heading='Festival Button Text'),
        ], heading="Home - Music Section"),
        MultiFieldPanel([
            ImageChooserPanel('workshops_cover', heading='Workshops Cover Image',),
            FieldPanel('workshops_heading', heading='Workshops Section Heading',),
            PageChooserPanel('workshops_page'),
            FieldPanel('workshops_button', heading='Workshops Button Text'),
        ], heading="Home - Music Section"),
    ]

    promote_panels = SeoMixin.seo_panels


    def get_context(self, request, *args, **kwargs):
        # Add Gateway videos to context
        context = super().get_context(request, self, *args, **kwargs)
        gateway = settings.CHRISTMAS
        video_list = services.get_video(gateway)

        context['gateway_video'] = video_list
        return context
