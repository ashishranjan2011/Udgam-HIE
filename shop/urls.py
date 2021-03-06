from django.conf.urls import url
from . import views
app_name="shop"
urlpatterns=[
    url(r'^$',views.product_list,name='product_list'),
    #url(r'^home/$' ,views.home,name='home'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
    ]

