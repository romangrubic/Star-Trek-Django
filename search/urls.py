from django.conf.urls import url
from .views import search_threads


urlpatterns = [
    url(r'^posts$', search_threads, name='search_threads'),
]
