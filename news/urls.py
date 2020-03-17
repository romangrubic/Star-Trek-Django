from django.conf.urls import url
from .views import get_news, news_detail, create_or_edit_news


urlpatterns = [
    url(r'^$', get_news, name='get_news'),
    url(r'^(?P<pk>\d+)/$', news_detail, name='news_detail'),
    url(r'^new/$', create_or_edit_news, name='new_news'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_news, name='edit_news')
]
