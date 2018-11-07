from django.conf.urls import url,include
from django.contrib import admin
from userpermission import  views as view
from journaltaks import views as j_vi


urlpatterns = [
    url(r'journal/', j_vi.journal),
    url(r'edit/(\d+)/', j_vi.edit),

]
