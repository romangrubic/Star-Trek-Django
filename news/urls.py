from django.conf.urls import url
from .views import get_news, news_detail, get_news_news, get_news_federation


urlpatterns = [
    url(r'^$', get_news, name='get_news'),
    url(r'^(?P<pk>\d+)/$', news_detail, name='news_detail'),
    url(r'^news$', get_news_news, name='get_news_news'),
    url(r'^federation$', get_news_federation, name='get_news_federation'),
]
