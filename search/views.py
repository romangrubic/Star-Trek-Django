from django.shortcuts import render
from products.models import Product
from posts.models import Post


# Create your views here.
def search_products(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})


def search_threads(request):
    threads = Post.objects.filter(tag__icontains=request.GET['d'])
    return render(request, "blogposts.html", {"posts": threads})
