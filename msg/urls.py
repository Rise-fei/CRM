from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve#需要导入
from django.conf import settings
from userpermission import urls as url_fei
from msg import urls as msg_url
from msg import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.msg),
    url(r'^newinst/', views.newinst),
]