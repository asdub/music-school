from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe


def charge(request):
    """ Create Stripe Payment Intent """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        print('Data:', request.POST)
        
        supportamount = request.POST['support-amount']
        amount = int(supportamount.replace(',', ''))
        name=request.POST['firstname'] + ' ' + request.POST['lastname']
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

        context = {
            'amount': amount,
            'customer': name,
            }
            
    return redirect(reverse('success'))



def successMsg(request, args):
    """ Return success message """
    amount = args
    return render(request, 'base/success.html', {'amount':amount})
