from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News
from .forms import NewsCommentForm
from django.contrib import messages


# Create your views here.
def get_news(request):
    """Create a view that will return a list of news"""
    news_list = News.objects.filter().order_by('-published_date')
    paginator = Paginator(news_list, 8)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, "newsblog.html", {'news': news})


def news_detail(request, pk):
    """Create a view that returns a single News object
    based on the news ID (pk) and render it """
    news = get_object_or_404(News, pk=pk)
    news.views += 1
    news.save()
    form = NewsCommentForm(request.POST, request.FILES)
    ctx = {'form': form}
    if form.is_valid():
        newscomment = form.save(commit=False)
        newscomment.news = news
        newscomment.user = request.user
        newscomment.profile_id = request.user.id
        newscomment.save()
        messages.success(request, 'You have successfuly left a comment at "%s" news!' % news.title)
        return redirect(news_detail, pk=news.id)
    return render(request, "newsdetail.html", {'news': news}, ctx)


def get_news_news(request):
    """Create a view that will return a list of news with tag: N (news) and
    render them"""
    news_list = News.objects.filter(tag='N')
    paginator = Paginator(news_list, 8)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, "newsblog.html", {'news': news})


def get_news_federation(request):
    """Create a view that will return a list of new with tag: F (federation) and
    render them"""
    news_list = News.objects.filter(tag='F')
    paginator = Paginator(news_list, 8)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, "newsblog.html", {'news': news})
