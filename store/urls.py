from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^product/(?P<product_id>[0-9]+)/buy$', views.buy, name='buy'),
    url(r'^product/(?P<product_id>[0-9]+)/delete', views.delete, name='buy'),
    url(r'^product/new/$', views.product_new, name='product_new'),
    url(r'^myproducts/$', views.user_products, name='myproducts'),
    # url(r'^user/(?P<user_id>[0-9]+)/products$', views.detail, name='user_products'),
]
