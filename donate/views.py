from django.conf import settings
from django.utils.timezone import make_aware

from django.shortcuts import redirect
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Donation

from wagtail.core.models import Page

import stripe
import datetime


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


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'charge.succeeded':
        print("Payment was successful.")
        customer = stripe.Customer.retrieve(event.data.object.customer)

        donation = Donation.objects.create(
            donation_id=event.data.object.id,
            date=make_aware(datetime.datetime.fromtimestamp(event.data.object.created)),
            status=event.data.object.status,
            customer_name=customer.name,
            customer_email=customer.email,
            donation_amount="€{:,.2f}".format(event.data.object.amount / 100),
            receipt_url=event.data.object.receipt_url,
            )
    return HttpResponse(status=200)


def new_donation(request):
    """ Set session var charge_success to false """
    source_page_id =request.POST.get('source-page-id')
    source_page = Page.objects.get(pk=source_page_id)

    request.session['charge_success'] = False
    return redirect(source_page.url , permanent=False)
