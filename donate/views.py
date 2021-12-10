from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

from wagtail.core.models import Page

import stripe


def charge(request):
    """ Create Stripe Payment Intent """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        source_page_id =request.POST.get('source-page-id')
        source_page = Page.objects.get(pk=source_page_id)

        supportamount = request.POST['support-amount']
        amount = int(supportamount.replace(',', ''))
        name = request.POST['firstname'] + ' ' + request.POST['lastname']
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=name,
            source=request.POST['stripeToken']
	    )
    
        charge = stripe.Charge.create(
			customer=customer,
			amount=amount,
			currency='eur',
			description=f"Donation from {name}"
			)

        hr_amount = "€{:,.2f}".format(amount / 100)

        context = {
            'amount': hr_amount,
            'customer': name,
            }

        request.session['charge_success'] = True
        request.session['charge'] = context
        return redirect(source_page.url, permanent=False)



def new_donation(request):
    """ Set session var charge_success to false """
    source_page_id =request.POST.get('source-page-id')
    source_page = Page.objects.get(pk=source_page_id)

    request.session['charge_success'] = False
    return redirect(source_page.url , permanent=False)
