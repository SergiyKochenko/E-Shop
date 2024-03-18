from django.shortcuts import render



def checkout(request):
        
        return render(request, 'payment/checkout.html')


def payment_success(request):

    # Clear shopping cart

    for key in list(request.session.keys()):

        if key == 'session_key':

            del request.session[key]

    return render(request, 'payment/payment-success.html')



def payment_failed(request):

    return render(request, 'payment/payment-failed.html')