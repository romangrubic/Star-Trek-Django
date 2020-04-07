from django.conf.urls import url
from .views import get_posts, post_detail, edit_post, create_post, get_posts_date, get_posts_title, get_posts_author


urlpatterns = [
    url(r'^views/$', get_posts, name='get_posts'),
    url(r'^date/$', get_posts_date, name='get_posts_date'),
    url(r'^title/$', get_posts_title, name='get_posts_title'),
    url(r'^author/$', get_posts_author, name='get_posts_author'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', edit_post, name='edit_post'),
]
