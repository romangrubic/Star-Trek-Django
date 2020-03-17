from django.conf.urls import url
from .views import games

urlpatterns = [
    url(r'^$', games, name='games')
]