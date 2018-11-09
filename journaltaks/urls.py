from django.conf.urls import url,include
from django.contrib import admin
from userpermission import  views as view
from journaltaks import views as j_vi


urlpatterns = [
    url(r'journal/', j_vi.journal),
    url(r'del_all/', j_vi.del_all),
    url(r'del_all2/', j_vi.del_all2),
    url(r'del_all3/', j_vi.del_all3),
    url(r'del_all4/', j_vi.del_all4),
    url(r'check_all/', j_vi.check_all),
    url(r'editJournal/id=(\d+)/', j_vi.editJournal),
    url(r'checkJournal/id=(\d+)/', j_vi.checkJournal),
    url(r'newJournal/', j_vi.newJournal),
    url(r'delJournal/id=(\d+)/', j_vi.delJournal),
    url(r'delManyJournal/', j_vi.delManyJournal),
    url(r'bespeak/', j_vi.bespeak),
    url(r'checkBespeak/id=(\d+)/', j_vi.checkBespeak),
    url(r'editBespeak/id=(\d+)/', j_vi.editBespeak),
    url(r'newBespeak/', j_vi.newBespeak),
    url(r'delBespeak/id=(\d+)/', j_vi.delBespeak),
    url(r'afterSale/', j_vi.afterSale),
    url(r'newAfterSale/', j_vi.newAfterSale),
    url(r'checkAfterSale/id=(\d+)/', j_vi.checkAfterSale),
    url(r'editAfterSale/id=(\d+)/', j_vi.editAfterSale),
    url(r'delAfterSale/id=(\d+)/', j_vi.delAfterSale),
    url(r'task/', j_vi.task),
    url(r'newTask/', j_vi.newTask),
    url(r'checkTask/id=(\d+)/', j_vi.checkTask),
    url(r'editTask/id=(\d+)/', j_vi.editTask),

]
