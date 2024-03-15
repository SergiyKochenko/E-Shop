
from django.shortcuts import redirect, render

from .forms import CreateUserForm

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid(): 

            user = form.save()

            return redirect('')



    context = {'form':form}


    return render(request, 'account/registration/register.html', context=context)
