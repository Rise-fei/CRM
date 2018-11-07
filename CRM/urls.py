"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from userpermission import  views as view
from journaltaks import views as j_vi
from django.views.static import serve#需要导入
from django.conf import settings
from userpermission import urls as url_fei
from journaltaks import urls as journal_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', view.index),
    url(r'^login/', view.login),
    url(r'^register/', view.register),
    url(r'^logout/', view.logout),


    url(r'^change_pw/(\d+)/', view.change_pw),
    url(r'^get_valid_img.png/', view.getValidImg),
    url(r'^userpermission/', include(url_fei)),
    url(r'^wang/', include(journal_url)),
]
