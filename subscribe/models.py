from django.db import models
from django.conf import settings
from django.shortcuts import redirect
import django.forms

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError



class SubscribeField(AbstractFormField):
    page = ParentalKey(
        'SubscribeForm',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class SubscribeForm(AbstractEmailForm):
    template = "includes/subscribe_form.html"
    landing_page_template = "includes/subscribe_form_landing.html"

    intro_text = RichTextField(blank=True)
    confirmation_text =  models.CharField(max_length=250, null=True)
    list_id =  models.CharField(max_length=100, null=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro_text', heading="Subscibe Form Text"),
        InlinePanel('form_fields', label='Subscribe Fields'),
        FieldPanel('confirmation_text', heading="Subscribe Confirmation Text"),
        FieldPanel('list_id', heading="Mailchimp List ID"),
    ]

    # Add placeholders to form fields
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for field in form.fields:
            form.fields[field].widget.attrs['placeholder'] = form.fields[field].help_text
            form.fields[field].widget.attrs['required'] = 'True'
        return form
        

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        source_page_id = request.POST.get('subscribe-page-id')
        list_id = request.POST.get('subscribe-list-id')
        email = request.POST.get('email')
        source_page = Page.objects.get(pk=source_page_id)

        try:
            client = MailchimpMarketing.Client()
            client.set_config({
            "api_key": settings.MAILCHIMP_API,
            "server": settings.MAILCHIMP_PREFIX
            })

            response = client.lists.add_list_member(list_id, {"email_address": email, "status": "subscribed"})
        except ApiClientError as error:
            print("Error: {}".format(error.text))

        if source_page:
            request.session['subscribe_success'] = True
            request.session['source-page'] = source_page.url
            return redirect(source_page.url  + '#subscribe', permanent=False)

        # if no source_page is set, render default landing page
        return super().render_landing_page(request, form_submission, *args, **kwargs)


