from django.db import models
from django.shortcuts import redirect
import django.forms

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactForm',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class CustomFormBuilder(FormBuilder):
    # Set textarea size
    def create_multiline_field(self, field, options):
        attrs = {'cols': '40', 'rows': '5'} # default attrs = {'cols': '40', 'rows': '10'}
        return django.forms.CharField(widget=django.forms.Textarea(attrs=attrs), **options)


class ContactForm(AbstractEmailForm):
    form_builder = CustomFormBuilder

    template = "includes/contact_form.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "includes/contact_form_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', heading="Form intro text"),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text', heading="Form submission/ thank you text"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),
    ]

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        source_page_id = request.POST.get('source-page-id')
        source_page = Page.objects.get(pk=source_page_id)

        if source_page:
            request.session['form_page_success'] = True
            request.session['source-page'] = source_page.url
            return redirect(source_page.url  + '#contact-us', permanent=False)

        # if no source_page is set, render default landing page
        return super().render_landing_page(request, form_submission, *args, **kwargs)
