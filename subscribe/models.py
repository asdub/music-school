from django.db import models
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

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro_text', heading="Subscibe Form Text"),
        InlinePanel('form_fields', label='Subscribe Fields'),
        FieldPanel('confirmation_text', heading="Subscribe Confirmation Text"),
    ]

    # Add placeholders to form fields
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for field in form.fields:
            form.fields[field].widget.attrs['placeholder'] = form.fields[field].help_text
        return form

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        source_page_id = request.POST.get('subscribe-page-id')
        source_page = Page.objects.get(pk=source_page_id)

        if source_page:
            request.session['subscribe_success'] = True
            request.session['source-page'] = source_page.url
            return redirect(source_page.url  + '#footer', permanent=False)

        # if no source_page is set, render default landing page
        return super().render_landing_page(request, form_submission, *args, **kwargs)

