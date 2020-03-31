from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product


# Create your views here.
def all_products(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})
    

def product_detail(request, pk):
    """Create a view that returns a single Post object
    based on the post ID (pk) and render it  to the
    'postdetail.html' template. Or return a 404 error if
    the post is not found """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {'product': product})
