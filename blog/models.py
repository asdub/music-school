from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class BlogIndexPage(Page):
    pass

class BlogPost(Page):
    date = models.DateField("Post Date")
    short_description = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    
    content_panels = [
        FieldPanel('title'),
        FieldPanel('date'),
        FieldPanel('short_description'),
        FieldPanel('body', classname="full"),
    ]