from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from userpermission import  models
from django.http import  JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
def getValidImg(request):
    # with open("valid_code.png", "rb") as f:
    #     data = f.read()
    # 自己生成一个图片
    from PIL import Image, ImageDraw, ImageFont
    import random

    # 获取随机颜色的函数
    def get_random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 生成一个图片对象
    img_obj = Image.new(
        'RGB',
        (220, 35),
        get_random_color()
    )
    # 在生成的图片上写字符
    # 生成一个图片画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 加载字体文件， 得到一个字体对象
    font_obj = ImageFont.truetype("static/font/AGaramondPro-Bold.otf", 28)
    # 开始生成随机字符串并且写到图片上
    tmp_list = []
    for i in range(5):
        u = chr(random.randint(65, 90))  # 生成大写字母
        l = chr(random.randint(97, 122))  # 生成小写字母
        n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型

        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20+40*i, 0), tmp, fill=get_random_color(), font=font_obj)

    print("".join(tmp_list))
    print("生成的验证码".center(120, "="))
    # 不能保存到全局变量
    # global VALID_CODE
    # VALID_CODE = "".join(tmp_list)

    # 保存到session
    request.session["valid_code"] = "".join(tmp_list)
    # 加干扰线
    # width = 220  # 图片宽度（防止越界）
    # height = 35
    # for i in range(5):
    #     x1 = random.randint(0, width)
    #     x2 = random.randint(0, width)
    #     y1 = random.randint(0, height)
    #     y2 = random.randint(0, height)
    #     draw_obj.line((x1, y1, x2, y2), fill=get_random_color())
    #
    # # 加干扰点
    # for i in range(40):
    #     draw_obj.point((random.randint(0, width), random.randint(0, height)), fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=get_random_color())

    # 将生成的图片保存在磁盘上
    # with open("s10.png", "wb") as f:
    #     img_obj.save(f, "png")
    # # 把刚才生成的图片返回给页面
    # with open("s10.png", "rb") as f:
    #     data = f.read()

    # 不需要在硬盘上保存文件，直接在内存中加载就可以
    from io import BytesIO
    io_obj = BytesIO()
    # 将生成的图片数据保存在io对象中
    img_obj.save(io_obj, "png")
    # 从io对象里面取上一步保存的数据
    data = io_obj.getvalue()
    return HttpResponse(data)



def change_pw(request,id):
    user_obj=models.UserInfo.objects.get(nid=id)
    if request.method=='POST':
        new_pw1=request.POST.get("new_pw1")
        new_pw2=request.POST.get("new_pw2")
        if new_pw1 == new_pw2:
            user_obj.set_password(new_pw1)
            user_obj.save()
            return redirect('/index/')
        else:
            return HttpResponse("新密码两次不一致")
    return render(request,'user_permission/change_pw.html',{"user":user_obj})

def edit_user(request,id):
    user_obj = models.UserInfo.objects.get(nid=id)
    if request.method=='POST':
        user_obj.username=request.POST.get('username')
        user_obj.set_password(request.POST.get('password'))
        employee_name=request.POST.get('employee_name')
        try:
             em_id=models.Employee.objects.get(employee_name=employee_name).id
             user_obj.employee_id = em_id
             user_obj.save()
        except:
            return HttpResponse('员工不存在，请查询后修改')
        return  redirect('/index/')

    return render(request,'user_permission/edit_user.html',{"user":user_obj})


def delete_user(request,id):
    user_obj=models.UserInfo.objects.get(nid=id)
    user_obj.delete()

    return redirect('/userpermission/user_manage')



def cat_user(request,id):
    user_obj=models.UserInfo.objects.get(nid=id)
    return render(request, 'user_permission/cat_user.html',{"user":user_obj})




def logout(request):
    auth.logout(request)
    return redirect('/index/')

@login_required
def accredit(request):
    role_list=models.Role.objects.all()

    if request.method=='POST':
        username=request.POST.get("username")
        role=request.POST.get("role")
        accedit_status=request.POST.get("accedit_status")

        role_obj=models.Role.objects.get(role_name=role)
        user_obj=models.UserInfo.objects.get(username=username)

        if accedit_status == '1':#状态为1   授权为  启动状态
            user_obj.status=1
        user_obj.role=role_obj
        user_obj.save()
        return redirect('/index/')

    return render(request,'user_permission/accredit.html',{"role_list":role_list,})

@login_required
def user_manage(request):

    user_list=models.UserInfo.objects.all()

    return render(request,'user_permission/user_manage.html',{"user_list":user_list})

def select(request):
    if request.method=='POST':
        username=request.POST.get("username")
        employee_name = request.POST.get("employee_name")
        try:
            user_employee_id=models.UserInfo.objects.get(username=username).employee_id
            em_objs=models.Employee.objects.filter(employee_name=employee_name)#防止重名
        except:
            ret = {"status": False}
            return JsonResponse(ret)
        for i in em_objs:
            if i.id == user_employee_id:  #说明用户名和员工姓名对应一个人
                department_name=models.Department.objects.get(id=i.department_id).department_name
                job_name=models.Job.objects.get(id=i.job_id).job_name
                # print(department_name)
                # print(job_name)
                ret={"department_name":department_name,
                     "job_name":job_name,
                     "status":True}
                return JsonResponse(ret)
        ret={"status":False}
    return JsonResponse(ret)


def index(request):
    user=request.user.username
    return render(request,'index.html',{"user":user})

def login(request):
    if request.method == 'POST':
    # if request.is_ajax():
        result={'status':0,'msg':''}
        username =request.POST.get('username')
        password = request.POST.get("password")
        valicode=request.POST.get('valid_code')
        if valicode and valicode.upper() == request.session.get('valid_code').upper():
            print('yes')
            user_obj = auth.authenticate(request, username=username, password=password)
            # user_obj=models.UserInfo.objects.filter(username=username)[0]
            if user_obj:
                auth.login(request,user_obj)
                result['msg']='/index/'
            else:
                # 用户名密码错误
                result["status"] = 1
                result["msg"] = "用户名或密码错误！"
        else:
            result['status']=1
            result["msg"] = "验证码错误！"
        return JsonResponse(result)
    return render(request,'user_permission/login.html')


def register(request):
    employee_list=models.Employee.objects.all()
    # print(employee_list)

    if request.method=='POST':
        email=request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        employee_id=request.POST.get('select_employee')
        if password1 == password2:

            models.UserInfo.objects.create_user(username=username, email=email, password=password2,employee_id=employee_id)
            return redirect('/login/')

        return HttpResponse("注册失败")

    return render(request,'user_permission/register.html',{"employee_list":employee_list})