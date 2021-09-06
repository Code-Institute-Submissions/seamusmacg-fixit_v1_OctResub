from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

def view_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect(reverse('products'))

    checkout_cart = cart_contents(request)
    total = checkout_cart['overall_cost']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'You are missing the Stripe public key.')

    order_form = OrderForm()
    context = {
             'order_form': order_form, 
             'stripe_public_key': stripe_public_key,
             'client_secret': intent.client_secret,
         }
         
    return render(request, 'checkout/checkout.html', context)




