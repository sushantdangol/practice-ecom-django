from django.urls import path
from . import views
from django.conf.urls import url
from .models import *

app_name='core'

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    # path('detail/<int:pk>/', views.product_detail, name='product_detail'),
]