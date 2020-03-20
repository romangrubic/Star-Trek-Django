from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})


def product_detail(request, pk):
    """Create a view that returns a single Post object
    based on the post ID (pk) and render it  to the
    'postdetail.html' template. Or return a 404 error if
    the post is not found """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {'product': product})
