from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from basket.models import Basket
from orders.models import Order, OrderItem

from orders.forms import CreateOrderForm


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Basket.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        requires_delivery= 0
                        if form.cleaned_data['delivery_address']:
                            requires_delivery = 1
                        print(form.cleaned_data['phone_number'])
                        print(requires_delivery)
                        print(form.cleaned_data['delivery_address'])
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=requires_delivery,
                            delivery_address=form.cleaned_data['delivery_address'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product=cart_item.product
                            name=cart_item.product.name
                            price=cart_item.product.price
                            quantity=cart_item.quantity

                            print(product)
                            print(name)
                            print(f"'{price}'")
                            print(quantity)
                            print(product.quantity)
                            print(order)

                            print(f"order: {order} type: {type(order)}")
                            print(f"product: {product} type: {type(product)}")
                            print(f"quantity: {quantity} type: {type(quantity)}")
                            print(f"product.quantity: {product.quantity} type: {type(product.quantity)}")


                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:basket')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('user:basket')
            
    return redirect('user:basket')