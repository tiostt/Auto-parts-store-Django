from basket.models import Basket


def get_user_carts(request):
    if request.user.is_authenticated:
        return Basket.objects.filter(user=request.user)