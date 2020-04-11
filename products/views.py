from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Review
from .forms import ReviewForm
from django.contrib import messages


# Create your views here.
def all_products(request):
    products_list = Product.objects.filter().order_by('-views')
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
    product.views += 1
    product.save()
    form = ReviewForm(request.POST, request.FILES)
    ctx = {'form': form}
    product_name = product.name
    if form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.user = request.user
        review.profile_id = request.user.id
        review.save()
        messages.success(request, 'You have successfuly left a review for "%s" product!' % product_name)
        return redirect(product_detail, pk=product.id)
    return render(request, "product_detail.html", {'product': product}, ctx)


def products_clothing(request):
    products_list = Product.objects.filter(tag="1")
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})


def products_accesories(request):
    products_list = Product.objects.filter(tag="2")
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})


def products_drinkware(request):
    products_list = Product.objects.filter(tag="3")
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})


def products_home_and_office(request):
    products_list = Product.objects.filter(tag="4")
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})


def products_collectibles(request):
    products_list = Product.objects.filter(tag="5")
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {"products": products})