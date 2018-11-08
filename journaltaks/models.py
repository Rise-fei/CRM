from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class Contact(models.Model):
    """
    联系人表
    """
    number = models.AutoField(primary_key=True, verbose_name="编号")
    contact_name = models.CharField(max_length=32, verbose_name="姓名")
    sex = models.CharField(max_length=32, verbose_name="性别")
    post = models.CharField(max_length=32, verbose_name="职务")
    contact_phone = models.CharField(max_length=11, verbose_name="手机号")
    email = models.EmailField(max_length=32, verbose_name="邮箱")

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name_plural = "联系人"


class Level(models.Model):
    """
    等级表
    """
    nid = models.AutoField(primary_key=True)
    level = models.CharField(max_length=32)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name_plural = "等级表"


class Organ(models.Model):
    """
    机构表
    """
    number = models.AutoField(primary_key=True, verbose_name="编号")
    name = models.CharField(max_length=32, verbose_name="机构名称")
    address = models.CharField(max_length=50, verbose_name="机构地址")
    organ_type = models.CharField(max_length=32, verbose_name="机构类型")
    contact = models.ForeignKey(to="Contact")  # 外键关联联系人表,一个机构可以对应多个联系人
    phone = models.CharField(max_length=11, verbose_name="手机号")
    website = models.CharField(max_length=50, verbose_name="网站")
    level = models.CharField(max_length=32, verbose_name="重要级别")
    grade = models.CharField(max_length=32, verbose_name="单位等级")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "机构表"


class JournalLevel(models.Model):
    nid = models.AutoField(primary_key=True)
    jou_level = models.CharField(max_length=32, verbose_name="日志等级")

    def __str__(self):
        return self.jou_level

    class Meta:
        verbose_name_plural = "日志等级"


class Journal(models.Model):
    """
    日志管理表
    """
    number = models.AutoField(primary_key=True, verbose_name="编号")
    personal = models.CharField(max_length=32, verbose_name="日志所属人")
    create_time = models.DateTimeField(verbose_name='日志日期', auto_now_add=True)
    content = models.TextField(max_length=500, verbose_name="日志内容")
    organ = models.ForeignKey(to="Organ")
    jou_level = models.ForeignKey(to="JournalLevel")

    def __str__(self):
        return self.personal

    class Meta:
        verbose_name_plural = "日志管理"


class ReservationState(models.Model):
    """
    预约状态表
    """
    nid = models.AutoField(primary_key=True)
    res_state = models.CharField(max_length=32, verbose_name="预约状态")

    def __str__(self):
        return self.res_state

    class Meta:
        verbose_name_plural = "预约状态"


class Bespeak(models.Model):
    """
    预约管理表
    """
    number = models.AutoField(primary_key=True, verbose_name="编号")
    organ = models.ForeignKey(to="Organ")
    create_time = models.DateTimeField(verbose_name='预约时间', auto_now_add=True)
    operator = models.CharField(max_length=32, verbose_name="操作人")
    content = models.TextField(max_length=500, verbose_name="预约内容")
    state = models.ForeignKey(to="ReservationState")
    data_time = models.DateTimeField(verbose_name="操作时间")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = "预约管理"


class SaleType(models.Model):
    """
    售后类型
    """
    nid = models.AutoField(primary_key=True)
    sale_type = models.CharField(max_length=32, verbose_name="售后类型")

    def __str__(self):
        return self.sale_type

    class Meta:
        verbose_name_plural = "售后类型"


class State(models.Model):
    """
    处理状态
    """
    nid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=32, verbose_name="处理状态")

    def __str__(self):
        return self.state

    class Meta:
        verbose_name_plural = "处理状态"


class AfterSale(models.Model):
    """
    售后日志表
    """
    number = models.AutoField(primary_key=True, verbose_name="编号")
    title = models.CharField(max_length=50, verbose_name="售后标题")
    sale_type = models.ForeignKey(to="SaleType")
    create_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    state = models.ForeignKey(to="State")
    content = models.TextField(max_length=5000, verbose_name="售后内容")
    contact_name = models.ForeignKey(to="Contact")
    organ = models.ForeignKey(to="Organ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "售后日志"


class ClassIfy(models.Model):
    """
    产品分类
    """
    nid = models.AutoField(primary_key=True)
    classify = models.CharField(max_length=32)

    def __str__(self):
        return self.classify

    class Meta:
        verbose_name_plural = "产品分类"


class Task(models.Model):
    """
    任务清单表
    """
    number = models.AutoField(primary_key=True, verbose_name="编号")
    organ = models.ManyToManyField(to="Organ", through="TaskOrgan")
    classify = models.ForeignKey(to="ClassIfy")
    Task_person = models.CharField(max_length=32, verbose_name="任务人员")
    content = models.TextField(max_length=500, verbose_name="任务内容")
    level = models.ForeignKey(to=Level)
    create_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    date_time = models.DateTimeField(verbose_name='操作时间', auto_now_add=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = "任务清单"


class TaskOrgan(models.Model):
    """
    任务机构多对多关系表
    """
    nid = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(to="Task")
    organ_id = models.ForeignKey(to="Organ")

    def __str__(self):
        return self.nid

    class Meta:
        verbose_name_plural = "任务--机构"
