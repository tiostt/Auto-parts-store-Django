from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from orders.models import Order
from users.forms import ProfileForm, UserLoginForm, UserRegistrarionForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы успешно вошли в аккаунт")
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    
    context = {
        'form': form
    }

    return render(request, 'users/vhod.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrarionForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрировались")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrarionForm()
    
    context = {
        'form': form
    }

    return render(request, 'users/registration.html', context)

@login_required
def basket(request):
    
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{request.user.username}, Вы успешно изменили данные")
            return HttpResponseRedirect(reverse('user:basket'))
    else:
        form = ProfileForm(instance=request.user)
    
    order = Order.objects.filter(user=request.user)
    
    context = {
        'form': form,
        'orders': order
    }

    return render(request, 'users/korzina.html', context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы успешно вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))