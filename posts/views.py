from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import BlogPostForm, CommentForm


# Create your views here.
def get_posts(request):
    """Create a view that will return a list of post and
    render them to the blogposts.html template"""
    post_list = Post.objects.filter(published_date__lte=timezone.now
                                ()).order_by('-published_date')
    paginator = Paginator(post_list, 15)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """Create a view that returns a single Post object
    based on the post ID (pk) and render it  to the
    'postdetail.html' template. Or return a 404 error if
    the post is not found """
    post = get_object_or_404(Post, pk=pk)
    #comments = get_object_or_404(Comment, post=post)
    
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post},)


@login_required()
def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.profile_id = request.user.id
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.profile_id = request.user.id
        comment.save()
        return redirect('post_detail', pk=post.id)
    return render(request, 'commentform.html', {'form': form}, )