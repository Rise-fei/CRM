from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    """
    用户信息表
    用户id  自增主键
    用户名 username
    创建日期 create_time
    角色分类（管理员分类） role  多对多
    用户员工  一对一            一个用户对应一个员工
    部门名称  department_name   一个用户对应一个员工，对应一个部门名称
    职位名称  job_name			一个用户对应一个员工，对应一个部门职位
    职务类别  job_category		一个职位对应一个职务类别
    授权状态                    根据用户角色权限表 查看
    """
    nid = models.AutoField(primary_key=True)
    create_time=models.DateTimeField(auto_now_add=True)
    employee=models.OneToOneField(to="Employee")
    status=models.BooleanField(default=False)
    role = models.ManyToManyField(to="Role",null=True)
class Employee(models.Model):
    '''
    员工表     employee
    Id
    员工编号
    员工姓名
    手机号码
    创建日期
    状态
    员工-部门    一个员工属于一个部门  外键
    员工-职位    一个员工对应一个职位  外键
    '''
    id=models.AutoField(primary_key=True)
    employee_name=models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    create_time = models.DateTimeField(auto_now_add=True)
    status=models.BooleanField()
    department=models.ForeignKey(to='Department')
    job=models.ForeignKey(to='Job')
class Department(models.Model):
    '''
    部门表    department
        Id
        部门名称
    '''
    id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=30)
class Job(models.Model):
    '''
    职位表    job
        Id
        职位名字   job_name
    '''
    id = models.AutoField(primary_key=True)
    job_name=models.CharField(max_length=30)

class Role(models.Model):
    nid=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=30)
    permission = models.ManyToManyField(to="Permission")


class Permission(models.Model):
    nid = models.AutoField(primary_key=True)
    permission_name=models.CharField(max_length=30)
    url=models.CharField(max_length=200)
    action=models.CharField(max_length=30,default="")
    group=models.ForeignKey(to="PermissionGroup",default=1)


class PermissionGroup(models.Model):
    title=models.CharField(max_length=30)
    def __str__(self):
        return self.title


class Essay_category(models.Model):
    category = models.CharField(max_length=30)
class File(models.Model):
    type=models.CharField(max_length=30)
class Essay(models.Model):
    essay_title=models.CharField(max_length=200)
    category=models.ForeignKey(to="Essay_category")
    file=models.ForeignKey(to="File")
    comment=models.TextField(max_length=300)
    author=models.CharField(max_length=30)
    file_file = models.FileField(default=None)
