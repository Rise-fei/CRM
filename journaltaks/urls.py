from django.conf.urls import url,include
from django.contrib import admin
from userpermission import  views as view
from journaltaks import views as j_vi


urlpatterns = [
    url(r'journal/', j_vi.journal),
    url(r'editJournal/id=(\d+)/', j_vi.editJournal),
    url(r'checkJournal/id=(\d+)/', j_vi.checkJournal),
    url(r'newJournal/', j_vi.newJournal),
    url(r'delJournal/id=(\d+)/', j_vi.delJournal),
    url(r'bespeak/', j_vi.bespeak),
    url(r'checkBespeak/id=(\d+)/', j_vi.checkBespeak),
    url(r'editBespeak/id=(\d+)/', j_vi.editBespeak),
    url(r'newBespeak/', j_vi.newBespeak),
    url(r'afterSale/', j_vi.afterSale),

]
