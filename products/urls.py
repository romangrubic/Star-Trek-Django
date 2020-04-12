from django.conf.urls import url
from .views import all_products, product_detail, products_clothing, products_accesories, products_drinkware, products_home_and_office, products_collectibles

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^clothing$', products_clothing, name='products_clothing'),
    url(r'^accesories$', products_accesories, name='products_accesories'),
    url(r'^drinkware$', products_drinkware, name='products_drinkware'),
    url(r'^home_and_office$', products_home_and_office, name='products_home_and_office'),
    url(r'^collectibles$', products_collectibles, name='products_collectibles'),
]
