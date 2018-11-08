from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from userpermission import models as model1
from django.http import JsonResponse
from django.db.models import Count
from msg import models as model2


# Create your views here.
def msg(request):
    res = model2.Inst.objects.all()

    return render(request, 'msg/inst_msg.html', {
        'inst': res
    })


def newinst(request):
    if request.method == 'POST':
        new_name = request.POST.get('iname')
        new_address = request.POST.get('iaddress')
        new_phone = request.POST.get('iphone')
        new_class = request.POST.get('iclass')
        new_status = request.POST.get('istatus')
        new_cname = request.POST.get('cname')
        new_cgender = request.POST.get('cgender')
        new_cjob = request.POST.get('cjob')
        new_cphone = request.POST.get('cphone')
        new_obj = model2.Inst.objects.create(
            name=new_name,
            address=new_address,
            phone=new_phone,
            iclass=new_class,
            istatus=new_status
        )
        new_cobj = model2.Contact.objects.create(
            cname=new_cname,
            cgender=new_cgender,
            cjob=new_cjob,
            cphone=new_cphone,
            inst=new_obj
        )
        return redirect('/msg/index/')
    return render(request, 'msg/new_inst_msg.html')


def edit_inst(request, new_id):
    if request.method == 'POST':
        new_name = request.POST.get('iname')
        new_address = request.POST.get('iaddress')
        new_phone = request.POST.get('iphone')
        new_class = request.POST.get('iclass')
        new_status = request.POST.get('istatus')
        new_cname = request.POST.get('cname')
        new_cgender = request.POST.get('cgender')
        new_cjob = request.POST.get('cjob')
        new_cphone = request.POST.get('cphone')
        new_obj = model2.Inst.objects.filter(id=new_id).first()
        new_obj.name = new_name
        new_obj.phone = new_phone
        new_obj.address = new_address
        new_obj.iclass = new_class
        new_obj.istatus = new_status
        new_obj.save()
        new_cobj = model2.Contact.objects.filter(inst=new_obj).first()
        if new_cobj:
            new_cobj.cname = new_cname
            new_cobj.cgender = new_cgender
            new_cobj.cjob = new_cjob
            new_cobj.cphone = new_cphone
            new_cobj.save()
        else:
            model2.Contact.objects.create(
                cname=new_cname,
                cgender=new_cgender,
                cphone=new_cphone,
                cjob=new_cjob,
                inst=new_obj
            )

        return redirect('/msg/index/')
    obj = model2.Inst.objects.filter(id=new_id).first()
    return render(request, 'msg/edit_inst_msg.html', {
        'obj': obj
    })


def del_inst(request, new_id):
    # new_id = request.GET.get('id')
    obj = model2.Inst.objects.get(id=new_id)
    obj.delete()
    return redirect('/msg/index/')


def inst_info(request, new_id):
    obj = model2.Inst.objects.get(id=new_id)
    return render(request, 'msg/inst_info.html', {
        'obj': obj
    })


def contact(request):
    obj = model2.Contact.objects.all()
    return render(request, 'msg/contact_msg.html', {
        'obj': obj
    })


def del_contact(request, new_id):
    obj = model2.Contact.objects.get(id=new_id)
    obj.delete()
    return redirect('/msg/contact/')


def chance_msg(request):
    obj = model2.Chance.objects.all()

    return render(request, 'msg/chance_msg.html', {
        'obj': obj
    })


def edit_chance(request, new_id):
    if request.method == 'POST':
        new_name = request.POST.get('iname')
        new_address = request.POST.get('iaddress')
        new_phone = request.POST.get('iphone')
        new_class = request.POST.get('iclass')
        new_status = request.POST.get('istatus')
        new_cname = request.POST.get('cname')
        new_cgender = request.POST.get('cgender')
        new_cjob = request.POST.get('cjob')
        new_cphone = request.POST.get('cphone')
        new_stage = request.POST.get('stage')
        new_fol = request.POST.get('fol')
        new_date = request.POST.get('date')
        new_money = request.POST.get('money')
        # 获取数据完毕
        new_obj = model2.Inst.objects.filter(id=new_id).first()
        # if new_obj:
        new_obj.name = new_name
        new_obj.phone = new_phone
        new_obj.address = new_address
        new_obj.iclass = new_class
        new_obj.istatus = new_status
        new_obj.save()
        # else:
        #     new_obj = model2.Inst.objects.create(
        #         name=new_name,
        #         phone=new_phone,
        #         address=new_address,
        #         iclass=new_class,
        #         istatus=new_status
        #     )
        new_cobj = model2.Contact.objects.filter(inst=new_obj).first()
        if new_cobj:
            new_cobj.cname = new_cname
            new_cobj.cgender = new_cgender
            new_cobj.cjob = new_cjob
            new_cobj.cphone = new_cphone
            new_cobj.save()
        else:
            model2.Contact.objects.create(
                cname=new_cname,
                cgender=new_cgender,
                cphone=new_cphone,
                cjob=new_cjob,
                inst=new_obj
            )
        new_chance = model2.Chance.objects.filter(inst=new_obj).first()
        if new_chance:
            new_chance.stage = new_stage
            new_chance.ctime = new_date
            print(new_date)
            print(type(new_date))
            new_chance.money = new_money
            new_chance.fol = new_fol
            new_chance.save()
        else:
            model2.Chance.objects.create(
                inst=new_obj,
                ctime=new_date,
                stage=new_stage,
                money=new_money,
                fol=new_fol
            )
        return redirect('/msg/chance/')
    obj = model2.Inst.objects.filter(id=new_id).first()
    return render(request, 'msg/edit_chance_msg.html', {
        'obj': obj
    })


def new_chance_msg(request):
    if request.method == 'POST':
        new_name = request.POST.get('iname')
        new_address = request.POST.get('iaddress')
        new_phone = request.POST.get('iphone')
        new_class = request.POST.get('iclass')
        new_status = request.POST.get('istatus')
        new_cname = request.POST.get('cname')
        new_cgender = request.POST.get('cgender')
        new_cjob = request.POST.get('cjob')
        new_cphone = request.POST.get('cphone')
        new_stage = request.POST.get('stage')
        new_fol = request.POST.get('fol')
        new_date = request.POST.get('date')
        new_money = request.POST.get('money')
        new_obj = model2.Inst.objects.filter(name=new_name).first()
        if new_obj:
            new_obj.name = new_name
            new_obj.phone = new_phone
            new_obj.address = new_address
            new_obj.istatus = new_status
            new_obj.iclass = new_class
            new_obj.save()
        else:
            new_obj = model2.Inst.objects.create(
                name=new_name,
                phone=new_phone,
                address=new_address,
                iclass=new_class,
                istatus=new_status
            )

        new_cobj = model2.Contact.objects.filter(inst=new_obj).first()
        if new_cobj:
            new_cobj.cname = new_cname
            new_cobj.cgender = new_cgender
            new_cobj.cjob = new_cjob
            new_cobj.cphone = new_cphone
            new_cobj.save()
        else:
            model2.Contact.objects.create(
                cname=new_cname,
                cgender=new_cgender,
                cphone=new_cphone,
                cjob=new_cjob,
                inst=new_obj
            )

        new_chance = model2.Chance.objects.filter(inst=new_obj).first()
        if new_chance:
            new_chance.stage = new_stage
            new_chance.ctime = new_date
            new_chance.money = new_money
            new_chance.fol = new_fol
        else:
            model2.Chance.objects.create(
                inst=new_obj,
                ctime=new_date,
                stage=new_stage,
                money=new_money,
                fol=new_fol
            )
        return redirect('/msg/chance/')

    return render(request, 'msg/new_chance_msg.html', )


def chance_query(request):
    msg1 = {'ms': 'hello'}
    if request.is_ajax():
        iname = request.POST.get('name')
        print(iname)
        obj = model2.Inst.objects.filter(name=iname).first()
        msg1['iaddress'] = obj.address
        msg1['iphone'] = obj.phone
        msg1['iclass'] = obj.iclass
        msg1['istatus'] = obj.istatus
        msg1['cname'] = obj.contact.cname
        msg1['cgender'] = obj.contact.cgender
        msg1['cjob'] = obj.contact.cjob
        msg1['cphone'] = obj.contact.cphone
        return JsonResponse(msg1)


def del_chance(request, new_id):
    new_obj = model2.Chance.objects.get(id=new_id)
    new_obj.delete()
    return redirect('/msg/chance/')


def product(request):
    obj = model2.Product.objects.all()
    return render(request, 'msg/product.html', {
        'obj': obj
    })


import time


def newpro(request):
    sid = request.GET.get('sid', None)
    sobj = model2.Product.objects.filter(id=sid).first()
    if request.method == 'POST':
        pname = request.POST.get('pname')
        inst_id = request.POST.get('inst_id')
        pkind = request.POST.get('pkind')
        pstage = request.POST.get('pstage')
        pstatus = request.POST.get('pstatus')
        # -----
        crname = request.POST.get('crname')
        crkind = request.POST.get('crkind')
        crstatus = request.POST.get('crstatus')
        crmoney = request.POST.get('crmoney')
        mdate = request.POST.get('mdate')
        signdate = request.POST.get('signdate')
        stdate = request.POST.get('stdate')
        endate = request.POST.get('endate')
        pobj = model2.Product.objects.filter(name=pname).first()
        print(pobj)
        if pobj:
            print('xiugai')
            pobj.name = pname
            pobj.inst_id = inst_id
            pobj.kind = pkind
            pobj.pstage = pstage
            pobj.pstatus = pstatus
            pobj.save()
        else:
            pobj = model2.Product.objects.create(
                name=pname,
                inst_id=inst_id,
                kind=pkind,
                pstage=pstage,
                pstatus=pstatus,
            )
        crobj = model2.Contract.objects.filter(name=crname).first()
        if crobj:
            crobj.product = pobj
            crobj.name = crname
            crobj.kind = crkind
            crobj.status = crstatus
            crobj.money = crmoney
            crobj.money_date = mdate
            crobj.sign_date = signdate
            crobj.start_date = stdate
            crobj.end_date = endate
            crobj.save()
        else:
            crobj = model2.Contract.objects.create(
                product=pobj,
                name=crname,
                kind=crkind,
                status=crstatus,
                money=crmoney,
                money_date=mdate,
                sign_date=signdate,
                start_date=stdate,
                end_date=endate,
            )
        return redirect('/msg/product/')
    return render(request, 'msg/newpro.html', {
        'obj': sobj
    })


def del_pro(request, new_id):
    new_obj = model2.Product.objects.get(id=new_id)
    new_obj.delete()
    return redirect('/msg/product/')


def info_pro(request, new_id):
    new_obj = model2.Product.objects.get(id=new_id)
    return render(request, 'msg/info_pro.html', {
        'obj': new_obj
    })


def contract(request):
    contract_obj = model2.Contract.objects.all()
    return render(request, 'msg/contract.html', {
        'obj': contract_obj
    })


def query_contract(request):
    if request.method == 'POST':
        select_text = request.POST.get('select_text')
        select_kind = request.POST.get('select_kind')
        if select_kind == '合同类型':
            obj = model2.Contract.objects.filter(kind__contains=select_text)
        elif select_kind == '合同名称':
            obj = model2.Contract.objects.filter(name__contains=select_text)
        elif select_kind == '机构名称':
            obj = model2.Contract.objects.filter(product__inst__name__contains=select_text)
        return render(request, 'msg/contract.html', {
            'obj': obj
        })
