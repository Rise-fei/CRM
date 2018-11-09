from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from userpermission import  models
from django.http import  JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
class Action(object):

    def __init__(self,actions):
        self.actions=actions

    def register(self):
        return "register" in self.actions
    def delete_user(self):
        return "delete_user" in self.actions
    def edit_user(self):
        return "edit_user" in self.actions
    def cat_user(self):
        return "cat_user" in self.actions
    def accredit(self):
        return "accredit" in self.actions

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


@login_required
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


@login_required
def edit_user(request,id):
    user_obj = models.UserInfo.objects.get(nid=id)
    action = Action(request.actions)
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

    return render(request,'user_permission/edit_user.html',{"user":user_obj,"action":action})

def edit_employee(request,id):
    print(id)
    employee=models.Employee.objects.get(id=id)
    department_list=models.Department.objects.all()
    job_list=models.Job.objects.all()
    action = Action(request.actions)
    if request.method=='POST':
        employee_name=request.POST.get("employee_name")
        phone=request.POST.get("phone")
        department_id=request.POST.get("department")
        job_id=request.POST.get("job")
        print(employee_name)
        print(phone)
        employee.employee_name=employee_name
        employee.phone=phone
        employee.department_id=department_id
        employee.job_id=job_id
        employee.save()

        return  redirect('/userpermission/employee_manage/')

    return render(request,'user_permission/edit_employee.html',locals())

@login_required
def delete_user(request,id):
    user_obj=models.UserInfo.objects.get(nid=id)
    action = Action(request.actions)
    user_obj.delete()

    return redirect('/userpermission/user_manage/',locals())
def delete_employee(request,id):
    employee_obj=models.Employee.objects.get(id=id)
    employee_obj.delete()
    return redirect('/userpermission/employee_manage/')

@login_required
def cat_user(request,id):
    user_obj=models.UserInfo.objects.get(nid=id)
    action = Action(request.actions)
    return render(request, 'user_permission/cat_user.html',{"user":user_obj,"action":action})
def cat_employee(request,id):
    employee=models.Employee.objects.get(id=id)
    action = Action(request.actions)
    return render(request, 'user_permission/cat_employee.html', locals())


def add_employee(request):
    department_list = models.Department.objects.all()
    job_list = models.Job.objects.all()
    if request.method=='POST':
        employee_name = request.POST.get("employee_name")
        phone = request.POST.get("phone")
        department_id = request.POST.get("department")
        job_id = request.POST.get("job")
        models.Employee.objects.create(employee_name=employee_name,phone=phone,department_id=department_id,job_id=job_id,status=0)
        return redirect('/userpermission/employee_manage/')
    return render(request,'user_permission/add_employee.html',locals())

def role_accredit(request):
    role_list=models.Role.objects.all()
    permission_list=models.Permission.objects.all()
    if request.method=='POST':
        role_id=request.GET.get("role_id")
        role_obj=models.Role.objects.get(nid=role_id)
        permission_list=request.POST.getlist("select_role_accredit")
        print(permission_list)
        role_obj.permission.clear()
        role_obj.permission.add(*permission_list)
        return redirect('/userpermission/role_accredit/')
    return render(request,'user_permission/role_accredit.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/index/')

@login_required
def accredit(request):
    role_list=models.Role.objects.all()
    if request.method=='POST':
        username=request.POST.get("username")
        employee_name=request.POST.get("employee_name")
        try:
            employee_obj=models.Employee.objects.get(employee_name=employee_name)
            user_obj=models.UserInfo.objects.get(username=username)

            employee_id=user_obj.employee_id
            if employee_obj.id == employee_id:
                user_obj.role.clear()  #清除之前对应的角色

                role_id_list=request.POST.getlist('select_role')
                # print(role_id_list)
                role_obj_list=models.Role.objects.filter(nid__in=role_id_list)
                user_obj.role.add(*role_obj_list)  #添加新的角色

                return redirect('/home/')
            else:
                return  HttpResponse("请输入匹配的用户名和员工名")
        except:
            return HttpResponse("请输入正确的用户名和员工名")

    return render(request,'user_permission/accredit.html',{"role_list":role_list,})

def employee_manage(request):
    employee_list=models.Employee.objects.all()

    return render(request,"user_permission/employee_manage.html",locals())
def essay_manage(request):
    essay_list=models.Essay.objects.all()
    return render(request,"user_permission/essay_manage.html",locals())

def add_essay(request):
    category_list=models.Essay_category.objects.all()
    file_list=models.File.objects.all()
    if request.method=='POST':
        essay_name=request.POST.get('essay_name')
        category_id=request.POST.get('category')
        file_id=request.POST.get('file')
        file_file=request.FILES.get('file_file')
        author=request.POST.get('author')
        comment=request.POST.get('comment')
        models.Essay.objects.create(essay_title=essay_name,author=author,comment=comment,
                                    category_id=category_id,file_id=file_id,
                                    file_file=file_file)
        return redirect('/userpermission/essay_manage/')
    return  render(request,'user_permission/add_essay.html',locals())


def edit_essay(request,essay_id):
    print(essay_id)
    essay_obj=models.Essay.objects.get(id=essay_id)
    category_list = models.Essay_category.objects.all()
    file_list = models.File.objects.all()
    if request.method == 'POST':
        essay_name = request.POST.get('essay_name')
        category_id = request.POST.get('category')
        file_id = request.POST.get('file')
        file_file = request.FILES.get('file_file')
        author = request.POST.get('author')
        comment = request.POST.get('comment')
        essay_obj.essay_title=essay_name
        essay_obj.author=author
        essay_obj.comment=comment
        essay_obj.category_id=category_id
        essay_obj.file_id=file_id
        essay_obj.file_file=file_file
        essay_obj.save()
        return redirect('/userpermission/essay_manage/')
    return render(request, 'user_permission/edit_essay.html', locals())
def cat_essay(request,id):
    essay_obj = models.Essay.objects.get(id=id)
    return render(request, 'user_permission/cat_essay.html', locals())
def delete_essay(request,id):
    essay_obj = models.Essay.objects.get(id=id)
    essay_obj.delete()
    return redirect('/userpermission/essay_manage/')
def select_essay(request):
    pass

@login_required
def user_manage(request):
    action = Action(request.actions)
    user_list=models.UserInfo.objects.all()


    return render(request,'user_permission/user_manage.html',{"user_list":user_list,"action":action})

def select(request):
    if request.method=='POST':
        username=request.POST.get("username")
        employee_name = request.POST.get("employee_name")
        print(username)
        print(employee_name)
        try:
            user_employee_id=models.UserInfo.objects.get(username=username).employee_id
            em_objs=models.Employee.objects.filter(employee_name=employee_name)#防止重名
            role_list = models.UserInfo.objects.get(username=username).role.all().values("role_name")
            print(role_list)
            role=[]
            for i in role_list:
                role.append(i["role_name"])
            print(role)
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
                     "role":role,
                     "status":True}
                return JsonResponse(ret)
        ret={"status":False}
    return JsonResponse(ret)

def home(request):
    return render(request,'user_permission/home.html')
def index(request):
    user=request.user.username
    return render(request,'index.html',{"user":user})
from userpermission.service.Permission import init_permission
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
            if user_obj:
                auth.login(request,user_obj)
                result['msg']='/home/'
                print(type(user_obj))
                print(user_obj.nid)
                request.session['user_id']=user_obj.nid

                init_permission(user_obj, request)
                # permissions=user_obj.role.all().values('permission__url').distinct()
                # print(permissions)
                # permission_list=[]
                # for i in permissions:
                #     permission_list.append(i["permission__url"])
                # print(permission_list)
                # request.session['permission_list']=permission_list
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
    employee_list=models.Employee.objects.filter(status=0)
    # role_list=models.Role.objects.all()
    # print(employee_list)

    if request.method=='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        employee_id=request.POST.get('select_employee')
        employee_obj = models.Employee.objects.get(id=employee_id)


        if password1 == password2:
            try:
                models.UserInfo.objects.create_user(username=username, password=password2,employee_id=employee_id)
                employee_obj.status = 1
                employee_obj.save()
            except:
                return HttpResponse('注册失败')
            return redirect('/home/')
        return HttpResponse("注册失败")
    return render(request,'user_permission/register.html',{"employee_list":employee_list,})