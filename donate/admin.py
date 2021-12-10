from django.shortcuts import redirect

from wagtail.contrib.modeladmin.helpers import ButtonHelper
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import Donation


class DonationAdmin(ModelAdmin):
    model = Donation
    menu_label = 'Donations'  # ditch this to use verbose_name_plural from model
    menu_icon = 'success'  # change as required
    menu_order = 000  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('date', 'customer_name', 'donation_amount', 'status')
    list_filter = ('status',)
    search_fields = ('customer_name', 'customer_email', 'donation_amount')

    def has_add_permission(self, request):
        return False


    def has_delete_permission(self, request, obj=None):
        return False


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(DonationAdmin)

