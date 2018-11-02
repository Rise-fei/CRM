from django.conf.urls import url,include
from django.contrib import admin
from userpermission import  views as views
from django.views.static import serve#需要导入
from django.conf import settings
urlpatterns = [

    url(r'^user_manage/', views.user_manage),
    url(r'^accredit/', views.accredit),
    url(r'^select/', views.select),
    url(r'^edit_user/(\d+)', views.edit_user),
    url(r'^delete_user/(\d+)', views.delete_user),
    url(r'^cat_user/(\d+)', views.cat_user),


]