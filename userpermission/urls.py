from django.conf.urls import url,include
from django.contrib import admin
from userpermission import  views as views
from django.views.static import serve#需要导入
from django.conf import settings
urlpatterns = [

    url(r'^user_manage/', views.user_manage),
    url(r'^accredit/', views.accredit),
    url(r'^select/', views.select),
    url(r'^edit_user/(\d+)/', views.edit_user),
    url(r'^delete_user/(\d+)/', views.delete_user),
    url(r'^cat_user/(\d+)/', views.cat_user),


    url(r'^employee_manage/', views.employee_manage),
    url(r'^edit_employee/(\d+)/', views.edit_employee),
    url(r'^delete_employee/(\d+)/', views.delete_employee),
    url(r'^cat_employee/(\d+)/', views.cat_employee),
]