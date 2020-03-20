from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, user_orders, edit_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^registration/$', registration, name="registration"),
    url(r'^profile/(?P<pk>\d+)/$', user_profile, name="profile"),
    url(r'^orders/$', user_orders, name="orders"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^profile/(?P<pk>\d+)/edit/$', edit_profile, name="edit_profile"),
]
