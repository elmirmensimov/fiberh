from django.urls import path, include
from . import views
from django.contrib import admin

from django.urls import path, include
from .views import convert_currency



urlpatterns = [

    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('convert_currency', views.convert_currency, name='convert_currency'),


]




