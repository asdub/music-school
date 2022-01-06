from django import template
from home.models import MyCustomSettings
from wagtail.core.models import Site

register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
def get_contact_form(context):
    request = context['request']
    my_custom_settings = MyCustomSettings.for_request(request)
    contact_form = my_custom_settings.contact_form.specific
    form = contact_form.get_form(
        page=contact_form, user=request.user)
    return {'page': contact_form, 'form': form}