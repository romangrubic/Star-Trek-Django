from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from django.contrib import messages


# Create your views here.
def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    product = get_object_or_404(Product, pk=id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    total = 0
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart

    for id, quantity, in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        request.session['total'] = float(total)
    messages.success(request, 'You have successfuly added - "%s" x %s unit(s) - to your shopping cart!' % (product.name, quantity))
    return redirect(reverse('products'))


def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    product = request.POST.get('product')

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
        messages.success(request, 'You have successfuly changed quantity of - "%s" - to %s unit(s)!' % (product, quantity))
    else:
        cart.pop(id)
        messages.error(request, 'You have successfuly removed - "%s" - from shopping cart!' % product)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
