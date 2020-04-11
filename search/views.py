from django.shortcuts import render, redirect
from products.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post
from posts.forms import BlogPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
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
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.profile_id = request.user.id
            post.save()
            messages.success(request, "You have successfuly added a new post!")
            return redirect('post_detail', post.pk)
    return render(request, "blogposts.html", {'posts': posts})
