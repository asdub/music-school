from django.db import models
import django.forms

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
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
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]
