from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse

from users.forms import ProfileForm

from .models import Basket
from .utils import get_user_carts
from catalog.models import Products


def basket_add(request):
    
    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user, product=product)

        if basket.exists():
            basket = basket.first()
            if basket:
                basket.quantity += 1
                basket.save()

        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)


    response_data = {
        "message": f"Товар \"{product.name}\" добавлен в корзину",
    }

    return JsonResponse(response_data)


def basket_change(request):
    
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")
    cart = Basket.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    
    form = ProfileForm(instance=request.user)

    user_cart = get_user_carts(request)

    context = {
        "baskets": user_cart,
        'form': form
    }

    cart_items_html = render_to_string(
        "users/korzina.html", context, request=request)

    response_data = {
        "message": "Количество товаров изменено",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def basket_remove(request):
    
    basket_id = request.POST.get("basket_id")
    print(basket_id)
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    form = ProfileForm(instance=request.user)

    user_cart = get_user_carts(request)
    context = {
        "baskets": user_cart,
        'form': form
    }
    cart_items_html = render_to_string(
        "users/korzina.html", context, request=request)

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
    }
    
    return JsonResponse(response_data)
