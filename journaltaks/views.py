from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import *
from journaltaks import models
from django.contrib import auth
from Myutils.pageutil import Page


# Create your views here.
def journal(request):
    journal_list = models.Journal.objects.all()
    page = Page(journal_list, request, 15, 10)
    sum = page.Sum()
    return render(request, 'journal_task/journal.html',
                  {'journal_list': sum[0], 'page_html': sum[1]})


def editJournal(request, number_id):
    journal_list = models.Journal.objects.filter(pk=number_id).first()
    jou_level_list = JournalLevel.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        organ_type = request.POST.get('organ_type')
        grade = request.POST.get('grade')
        address = request.POST.get('address')
        contact_name = request.POST.get('contact_name')
        contact_phone = request.POST.get('contact_phone')
        personal = request.POST.get('personal')
        jou_level_id = request.POST.get('jou_level_id')
        content = request.POST.get('content')
        create_time = request.POST.get('create_time')
        org_id = models.Journal.objects.filter(pk=number_id)[0].organ_id
        con_id = models.Organ.objects.filter(pk=org_id)[0].contact_id
        print(org_id)
        print(con_id)
        if personal or jou_level_id or content or create_time:
            Journal.objects.filter(pk=number_id).update(personal=personal, jou_level_id=jou_level_id, content=content,
                                                        create_time=create_time)
        if contact_name or contact_phone:
            Contact.objects.filter(pk=con_id).update(contact_name=contact_name, contact_phone=contact_phone)
        if name or organ_type or grade or address:
            Organ.objects.filter(pk=org_id).update(name=name, organ_type=organ_type, grade=grade, address=address)

        return redirect('/wang/journal/')
    return render(request, 'journal_task/editJournal.html',
                  {'journal_list': journal_list,
                   'jou_level_list': jou_level_list,
                   })


def checkJournal(request, number_id):
    check_list = models.Journal.objects.filter(pk=number_id).first()
    return render(request, 'journal_task/checkJournal.html', {'check_list': check_list})


def newJournal(request):
    jou_level_list = JournalLevel.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        organ_type = request.POST.get('organ_type')
        grade = request.POST.get('grade')
        address = request.POST.get('address')
        contact_name = request.POST.get('contact_name')
        contact_phone = request.POST.get('contact_phone')
        personal = request.POST.get('personal')
        jou_level_id = request.POST.get('jou_level_id')
        content = request.POST.get('content')
        create_time = request.POST.get('create_time')
        con_obj = Contact.objects.create(contact_name=contact_name, contact_phone=contact_phone)
        org_obj = Organ.objects.create(contact=con_obj, name=name, organ_type=organ_type, grade=grade, address=address)
        jou_obj = Journal.objects.create(jou_level_id=jou_level_id, organ=org_obj, personal=personal, content=content,
                                         create_time=create_time)
        return redirect('/wang/journal/')
    return render(request, 'journal_task/newJournal.html', {'jou_level_list': jou_level_list})


def delJournal(request, del_id):
    # 判断删除数据是否为空
    print(del_id)
    if del_id:
        del_obj = models.Journal.objects.filter(pk=del_id)
        del_obj.delete()
        return redirect('/wang/journal/')
    return HttpResponse('ok')


def delManyJournal(request):
    check_list = request.POST.getlist('onclick_checkbox')
    print(check_list)
    return render(request, 'journal_task/journal.html')


def bespeak(request):
    bespeak_list = models.Bespeak.objects.all()
    return render(request, 'journal_task/bespeak.html', {'bespeak_list': bespeak_list})


def checkBespeak(request, number_id):
    check_list = models.Bespeak.objects.filter(pk=number_id).first()
    return render(request, 'journal_task/checkBespeak.html', {'check_list': check_list})


def editBespeak(request, number_id):
    print(number_id)
    bespeak_list = models.Bespeak.objects.filter(pk=number_id).first()
    organ_list = models.Organ.objects.all()
    state_list = models.ReservationState.objects.all()
    if request.method == 'POST':
        organ_id = request.POST.get("organ_id")
        create_time = request.POST.get("create_time")
        operator = request.POST.get("operator")
        state_id = request.POST.get("state_id")
        data_time = request.POST.get("data_time")
        Bespeak.objects.filter(pk=number_id).update(organ_id=organ_id, create_time=create_time, operator=operator,
                                                    state_id=state_id, data_time=data_time)
        return redirect('/wang/bespeak/')
    return render(request, 'journal_task/editBespeak.html',
                  {'bespeak_list': bespeak_list, 'organ_list': organ_list, 'state_list': state_list})


def newBespeak(request):
    organ_list = models.Organ.objects.all()
    state_list = models.ReservationState.objects.all()
    bespeak_list = Bespeak.objects.all()
    if request.method == 'POST':
        organ_id = request.POST.get("organ_id")
        create_time = request.POST.get("create_time")
        operator = request.POST.get("operator")
        state_id = request.POST.get("state_id")
        data_time = request.POST.get("data_time")
        print(state_id)
        bes_obj = Bespeak.objects.create(organ_id=organ_id, create_time=create_time, operator=operator,
                                         data_time=data_time, state_id=state_id)
        return redirect('/wang/bespeak/')
    return render(request, 'journal_task/newBespeak.html',
                  {'organ_list': organ_list, 'state_list': state_list, 'bespeak_list': bespeak_list})


def delBespeak(request, del_id):
    # 判断删除数据是否为空
    print(del_id)
    if del_id:
        del_obj = models.Bespeak.objects.filter(pk=del_id)
        del_obj.delete()
        return redirect('/wang/bespeak/')
    return HttpResponse('ok')


def afterSale(request):
    after_sale_list = models.AfterSale.objects.all()
    return render(request, 'journal_task/afterSale.html', {'after_sale_list': after_sale_list})


def newAfterSale(request):
    organ_list = Organ.objects.all()
    sale_type_list = SaleType.objects.all()
    contact_list = Contact.objects.all()
    state_list = State.objects.all()
    after_sale_list = AfterSale.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        organ_id = request.POST.get("organ_id")
        sale_type_id = request.POST.get("sale_type_id")
        contact_name_id = request.POST.get("contact_name_id")
        create_time = request.POST.get("create_time")
        state_id = request.POST.get("state_id")
        after_sale_obj = AfterSale.objects.create(title=title, organ_id=organ_id, sale_type_id=sale_type_id,
                                                  contact_name_id=contact_name_id, create_time=create_time,
                                                  state_id=state_id)
        return redirect('/wang/afterSale/')
    return render(request, 'journal_task/newAfterSale.html',
                  {'after_sale_list': after_sale_list, 'organ_list': organ_list,
                   'sale_type_list': sale_type_list, 'contact_list': contact_list,
                   'state_list': state_list})


def checkAfterSale(request, number_id):
    check_list = models.AfterSale.objects.filter(pk=number_id).first()
    return render(request, 'journal_task/checkAfterSale.html', {'check_list': check_list})


def editAfterSale(request, number_id):
    organ_list = Organ.objects.all()
    sale_type_list = SaleType.objects.all()
    contact_list = Contact.objects.all()
    state_list = State.objects.all()
    check_after_list = AfterSale.objects.filter(pk=number_id).first()
    if request.method == 'POST':
        title = request.POST.get("title")
        organ_id = request.POST.get("organ_id")
        sale_type_id = request.POST.get("sale_type_id")
        contact_name_id = request.POST.get("contact_name_id")
        state_id = request.POST.get("state_id")
        content = request.POST.get("content")
        aft_obj = AfterSale.objects.filter(pk=number_id).update(title=title, organ_id=organ_id,
                                                                sale_type_id=sale_type_id,
                                                                contact_name_id=contact_name_id,
                                                                state_id=state_id, content=content)
        return redirect('/wang/afterSale/')
    return render(request, 'journal_task/editAfterSale.html',
                  {'check_after_list': check_after_list, 'organ_list': organ_list,
                   'sale_type_list': sale_type_list, 'contact_list': contact_list,
                   'state_list': state_list})


def delAfterSale(request, del_id):
    # 判断删除数据是否为空
    print(del_id)
    if del_id:
        del_obj = models.AfterSale.objects.filter(pk=del_id)
        del_obj.delete()
        return redirect('/wang/afterSale/')
    return HttpResponse('ok')


def task(request):
    task_obj = Task.objects.all()
    page = Page(task_obj, request, 15, 10)
    sum = page.Sum()
    return render(request, 'journal_task/task.html',
                  {'task_obj': sum[0], 'page_html': sum[1]})


def checkTask(request, number_id):
    task_obj = Task.objects.filter(pk=number_id).first()
    return render(request, 'journal_task/checkTask.html',
                  {'task_obj': task_obj})


def editTask(request, number_id):
    task_obj = Task.objects.filter(pk=number_id).first()
    return render(request, 'journal_task/editTask.html',
                  {'task_obj': task_obj})


def newTask(request):
    organ_list = Organ.objects.all()
    level_list = Level.objects.all()
    classify_list = ClassIfy.objects.all()
    task_obj = Task.objects.all()
    return render(request, 'journal_task/newTask.html',
                  {'task_obj': task_obj, 'organ_list': organ_list,
                   'level_list': level_list, 'classify_list': classify_list})


def del_all(request):
    if request.method == 'POST':
        val_obj = request.POST.getlist("check_val")
        print(val_obj)
        if val_obj:
            for i in val_obj:
                print(i)
                del_obj = models.Journal.objects.filter(pk=i)
                del_obj.delete()
        return render(request, 'journal_task/journal.html')
    return render(request, 'journal_task/journal.html')


def del_all2(request):
    if request.method == 'POST':
        val_obj = request.POST.getlist("check_val")
        print(val_obj)
        if val_obj:
            for i in val_obj:
                print(i)
                del_obj = models.Bespeak.objects.filter(pk=i)
                del_obj.delete()
        return render(request, 'journal_task/bespeak.html')
    return render(request, 'journal_task/bespeak.html')


def del_all3(request):
    if request.method == 'POST':
        val_obj = request.POST.getlist("check_val")
        print(val_obj)
        if val_obj:
            for i in val_obj:
                print(i)
                del_obj = models.AfterSale.objects.filter(pk=i)
                del_obj.delete()
        return render(request, 'journal_task/afterSale.html')
    return render(request, 'journal_task/afterSale.html')


def del_all4(request):
    if request.method == 'POST':
        val_obj = request.POST.getlist("check_val")
        print(val_obj)
        if val_obj:
            for i in val_obj:
                print(i)
                del_obj = models.Task.objects.filter(pk=i)
                del_obj.delete()
        return render(request, 'journal_task/task.html')
    return render(request, 'journal_task/task.html')


def check_all(request):
    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        select_text = request.POST.get('select_text')
        if select_text == '1':
            journal_list = models.Journal.objects.filter(organ__name__contains=search_key)
            return render(request, 'journal_task/check_all.html', {'journal_list': journal_list})
        elif select_text == '2':
            journal_list = models.Journal.objects.filter(organ__organ_type__contains=search_key)
            return render(request, 'journal_task/check_all.html', {'journal_list': journal_list})
        elif select_text == '3':
            journal_list = models.Journal.objects.filter(personal__contains=search_key)
            return render(request, 'journal_task/check_all.html', {'journal_list': journal_list})
        elif select_text == '4':
            journal_list = models.Journal.objects.filter(organ__contact__contact_name__contains=search_key)
            return render(request, 'journal_task/check_all.html', {'journal_list': journal_list})
        elif select_text == '5':
            journal_list = models.Journal.objects.filter(jou_level__jou_level__contains=search_key)
            return render(request, 'journal_task/check_all.html', {'journal_list': journal_list})
    return render(request, 'journal_task/journal.html')
