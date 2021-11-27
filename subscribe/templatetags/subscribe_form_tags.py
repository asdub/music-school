from django import template
from home.models import SubscribeSettings
from wagtail.core.models import Site

register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
def get_subscribe_form(context):
    request = context['request']
    my_custom_settings = SubscribeSettings.for_request(request)
    subscribe_form = my_custom_settings.subscribe_form.specific
    form = subscribe_form.get_form(
        page=subscribe_form, user=request.user)
    return {'page': subscribe_form, 'subscribe_form': form}