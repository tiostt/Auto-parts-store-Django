from django.core.paginator import Paginator
from django.shortcuts import render

from .utils import q_search

from .models import Products


def catalog(request):

    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    products = Products.objects.all()

    if query:
        products = q_search(query)

    if order_by:
        products = products.order_by(order_by)

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    context ={
        'products': current_page,
    }

    return render(request, 'catalog/index1.html', context)

def product(request, product_slug):
    
    products = Products.objects.get(slug=product_slug)
    
    context ={
        'products': products,
    }

    return render(request, 'catalog/tovar.html', context)