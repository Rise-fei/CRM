from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class Contact(models.Model):
    """
    联系人表
    """
    nid = models.AutoField(primary_key=True)
    content_name = models.CharField(max_length=32, verbose_name="姓名")
    sex = models.CharField(max_length=32, verbose_name="性别")
    post = models.CharField(max_length=32, verbose_name="职务")
    phone = models.IntegerField(verbose_name="手机号")
    email = models.EmailField(max_length=32, verbose_name="邮箱")


class Organ(models.Model):
    """
    机构表
    """
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="机构名称")
    address = models.CharField(max_length=50, verbose_name="机构地址")
    organ_type = models.CharField(max_length=32, verbose_name="机构类型")
    contact = models.ForeignKey(to="Contact", to_field="nid")  # 外键关联联系人表,一个机构可以对应多个联系人
    phone = models.IntegerField(verbose_name="手机号")
    website = models.CharField(max_length=50, verbose_name="网站")
    level = models.CharField(max_length=32, verbose_name="重要级别")
    grade = models.CharField(max_length=32, verbose_name="单位等级")


class Journal(models.Model):
    """
    日志管理表
    """
    nid = models.AutoField(primary_key=True)
    number = models.IntegerField(verbose_name="编号")
    personal = models.CharField(max_length=32, verbose_name="日志所属人")
    create_time = models.DateTimeField(verbose_name='日志日期', auto_now_add=True)
    content = models.TextField(max_length=500, verbose_name="日志内容")
    organ = models.OneToOneField(to="Organ")
    jou_level = models.CharField(max_length=32, verbose_name="日志等级")


class ReservationState(models.Model):
    """
    预约状态表
    """
    nid = models.AutoField(primary_key=True)
    res_state = models.CharField(max_length=32, verbose_name="预约状态")


class Bespeak(models.Model):
    """
    预约管理表
    """
    nid = models.AutoField(primary_key=True)
    number = models.IntegerField(verbose_name="编号")
    organ = models.OneToOneField(to="Organ")
    create_time = models.DateTimeField(verbose_name='预约时间', auto_now_add=True)
    operator = models.CharField(max_length=32, verbose_name="操作人")
    state = models.OneToOneField(to="ReservationState", to_field="nid")
    data_time = models.DateField(verbose_name="操作时间")


class AfterSale(models.Model):
    """
    售后日志表
    """
    nid = models.AutoField(primary_key=True)
    number = models.IntegerField(verbose_name="编号")
    title = models.CharField(max_length=50, verbose_name="售后标题")
    sale_type = models.CharField(max_length=32, verbose_name="售后类型")
    create_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    state = models.CharField(max_length=32, verbose_name="处理状态")
    organ_after_sale = models.ManyToManyField(
        to="Organ",
        through="OrganAfterSale",
    )


class OrganAfterSale(models.Model):
    """
    售后与机构多对多关系表
    """
    nid = models.AutoField(primary_key=True)
    organ_id = models.ForeignKey(to="Organ", to_field="nid")
    after_sale_id = models.ForeignKey(to="AfterSale", to_field="nid")


class Task(models.Model):
    """
    任务清单表
    """
    nid = models.AutoField(primary_key=True)
    number = models.IntegerField(verbose_name="编号")
    organ = models.OneToOneField(to="Organ",)
    classify = models.CharField(max_length=32, verbose_name="产品分类")
    Task_person = models.CharField(max_length=32, verbose_name="任务人员")
    level = models.CharField(max_length=32, verbose_name="任务级别")
    create_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    date_time = models.DateTimeField(verbose_name='操作时间', auto_now_add=True)
