from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve  # 需要导入
from django.conf import settings
from userpermission import urls as url_fei
from msg import urls as msg_url
from msg import views

urlpatterns = [
    url(r'^index/', views.msg),
    url(r'^newinst/', views.newinst),
    url(r'^edit_inst/(\d+)', views.edit_inst),
    url(r'^del_inst/(\d+)', views.del_inst),
    url(r'^inst_info/(\d+)', views.inst_info),
    url(r'^contact/', views.contact),
    url(r'^del_cont/(\d+)', views.del_contact),
    url(r'^chance/', views.chance_msg),
    url(r'^edit_chance/(\d+)', views.edit_chance),
    url(r'^new_chance/', views.new_chance_msg),
    url(r'^chance_query/', views.chance_query),
    url(r'^del_chance/(\d+)', views.del_chance),
    url(r'^product/', views.product),
    url(r'^contract/', views.contract),
    url(r'^newpro/', views.newpro),
    url(r'^del_pro/(\d+)', views.del_pro),
    url(r'^info_pro/(\d+)', views.info_pro),
    url(r'^query_contract/', views.query_contract),
    url(r'^query_pro/', views.query_pro),
    url(r'^query_chance/', views.query_chance),
    url(r'^query_inst/', views.query_inst),

    # url(r'^newcontact/', views.new_contact),

]
