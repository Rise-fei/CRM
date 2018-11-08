from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from journaltaks import models
from django.contrib import auth


# Create your views here.
def journal(request):
    journal_list = models.Journal.objects.all()
    return render(request, 'journal_task/journal.html', {'journal_list': journal_list})


def editJournal(request, nid):
    print(nid)
    journal_list = models.Journal.objects.filter(nid=nid).first()
    if request.method == 'POST':
        name = request.POST.get('name')
        organ_type = request.POST.get('organ_type')
        grade = request.POST.get('grade')
        address = request.POST.get('address')
        content_name = request.POST.get('content_name')
        phone = request.POST.get('phone')
        personal = request.POST.get('personal')
        jou_level = request.POST.get('jou_level')
        content = request.POST.get('content')
        create_time = request.POST.get('create_time')
        models.Journal.objects.filter(nid=nid).update(name=name, organ_type=organ_type, grade=grade, address=address,
                                                      content_name=content_name, phone=phone, personal=personal,
                                                      jou_level=jou_level, content=content, create_time=create_time)
        return HttpResponse('OK')
    print(journal_list)
    return render(request, 'journal_task/editJournal.html', {'journal_list': journal_list})


def checkJournal(request, nid):
    check_list = models.Journal.objects.filter(nid=nid).first()
    return render(request, 'journal_task/checkJournal.html', {'check_list': check_list})


def newJournal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        organ_type = request.POST.get('organ_type')
        grade = request.POST.get('grade')
        address = request.POST.get('address')
        content_name = request.POST.get('content_name')
        phone = request.POST.get('phone')
        personal = request.POST.get('personal')
        jou_level = request.POST.get('jou_level')
        content = request.POST.get('content')
        create_time = request.POST.get('create_time')
        models.Journal.objects.create(name=name, organ_type=organ_type, grade=grade, address=address,
                                      content_name=content_name, phone=phone, personal=personal,
                                      jou_level=jou_level, content=content, create_time=create_time)
        return render(request, 'journal_task/journal.html')
    return render(request, 'journal_task/newJournal.html')


def delJournal(request, nid):
    # 获取需要删除的数据ID
    del_id = request.GET.get("nid")
    # 判断删除数据是否为空
    print(del_id)
    if del_id:
        del_obj = models.Journal.objects.get(nid=del_id)
        del_obj.delete()
        return redirect('/journal/')
    return HttpResponse('ok')


def bespeak(request):
    bespeak_list = models.Bespeak.objects.all()
    return render(request, 'journal_task/bespeak.html', {'bespeak_list': bespeak_list})


def checkBespeak(request, nid):
    check_list = models.Bespeak.objects.filter(nid=nid).first()
    return render(request, 'journal_task/checkBespeak.html', {'check_list': check_list})


def editBespeak(request, nid):
    print(nid)
    bespeak_list = models.Bespeak.objects.filter(nid=nid).first()
    if request.method == 'POST':
        return HttpResponse('OK')
    return render(request, 'journal_task/editBespeak.html', {'bespeak_list': bespeak_list})


def newBespeak(request):
    return render(request, 'journal_task/newBespeak.html')


def afterSale(request):
    after_sale_list = models.AfterSale.objects.all()
    return render(request, 'journal_task/afterSale.html', {'after_sale_list': after_sale_list})
