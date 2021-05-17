from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from .views import product_view, register_view, delete_product_view, data_product_view
from .views import update_product_view, create_product_view, home_view, order_product_name_view
from .views import order_product_price_view, order_product_stock_view


urlpatterns = [
    url('products', product_view, name='products'),
    url('register', register_view, name='register'),
    url(r'^delete_product/(?P<pk>.*)', delete_product_view, name='del'),
    url(r'^edit_product/(?P<pk>.*)', update_product_view, name='edit'),
    url('create_product', create_product_view, name='create-product'),
    url('home', home_view, name='home'),
    url('graphicdata', data_product_view, name='graphicdata'),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^order_name/', order_product_name_view, name='order_name'),
    url(r'^order_price/', order_product_price_view, name='order_price'),
    url(r'^order_stock/', order_product_stock_view, name='order_stock'),
    url('', TemplateView.as_view(template_name='index.html'), name='index'),
]
# NoReverseMatch: Reverse for 'del' with arguments '(1,)' not found. 1 pattern(s) tried: ['delete_product/<int:pk>']

