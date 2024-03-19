from django.shortcuts import render

from . models import ShippingAddress



def checkout(request):

    if request.user.is_authenticated:

        try:

            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {'shipping': shipping_address}

            return render(request, 'payment/checkout.html', context=context)

        except:

            return render(request, 'payment/checkout.html')

    else:

        return render(request, 'payment/checkout.html')



def payment_success(request):

    # Clear shopping cart

    for key in list(request.session.keys()):

        if key == 'session_key':

            del request.session[key]

    return render(request, 'payment/payment-success.html')



def payment_failed(request):

    return render(request, 'payment/payment-failed.html')