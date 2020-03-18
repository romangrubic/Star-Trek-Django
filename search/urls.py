from django.conf.urls import url
from .views import search_products, search_threads


urlpatterns = [
    url(r'^products$', search_products, name='search_products'),
    url(r'^posts$', search_threads, name='search_threads'),
]
