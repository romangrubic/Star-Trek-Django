from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post


# Create your views here.
def search_threads(request):
    post_list = Post.objects.filter(title__icontains=request.GET['d']).order_by('-views')
    paginator = Paginator(post_list, 15)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blogposts.html", {'posts': posts})
