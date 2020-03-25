from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post, add_comment, get_posts_date


urlpatterns = [
    url(r'^views/$', get_posts, name='get_posts'),
    url(r'^date/$', get_posts_date, name='get_posts_date'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/comment/$', add_comment, name='add_comment'),
]
