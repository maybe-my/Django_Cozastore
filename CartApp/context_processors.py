from .cart import Cart


def cart(request):
    return {'CartApp': Cart(request)}
