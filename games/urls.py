from django.conf.urls import url
from .views import games, games_detail

urlpatterns = [
    url(r'^$', games, name='games'),
    url(r'^(?P<pk>\d+)/$', games_detail, name='games_detail'),
]
