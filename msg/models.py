from django.db import models
import time


# Create your models here.
# 机构信息
class Inst(models.Model):  # 机构
    name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=20, null=True, blank=True, default='qd')
    phone = models.CharField(max_length=13, unique=True)
    iclass = models.CharField(max_length=5, null=False)
    istatus = models.CharField(max_length=5, choices=(('未审核', '未审核'), ('已审核', '已审核')), default='未审核')


class Contact(models.Model):  # 联系人
    cname = models.CharField(max_length=20)  # 姓名
    cgender = models.CharField(max_length=1, null=False)  # 性别
    cjob = models.CharField(max_length=10, null=True, blank=True, default='cb')  # 职位
    cphone = models.CharField(max_length=13, unique=True)  # 手机
    inst = models.OneToOneField(to=Inst)  # 一对一关联机构表


class Chance(models.Model):  # 商机
    stage = models.CharField(max_length=10)  # 阶段状态
    fol = models.CharField(max_length=5)  # 跟进状态
    money = models.DecimalField(max_digits=10, decimal_places=2)  # 年费
    ctime = models.DateField(auto_now=True)  # 购买时间
    inst = models.OneToOneField(to=Inst)  # 一对一关联机构表
    # 差一个经办人


class Product(models.Model):  # 产品
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=8)  # 产品分类  网站 APP 微刊
    pstage = models.CharField(max_length=5)  # 产品状态
    pstatus = models.CharField(max_length=8)  # 产品使用状态
    inst = models.OneToOneField(to=Inst)


class Contract(models.Model):  # 合同
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=8)  # 合同分类  销售 采购
    status = models.CharField(max_length=8)  # 合同状态  新增 意向 已签  续约
    money = models.DecimalField(max_digits=10, decimal_places=2)  # 合同总金额
    money_date = models.DateField()  # 最后付款期限
    sign_date = models.DateField()  # 签约时间
    start_date = models.DateField()  # 开始时间
    end_date = models.DateField()  # 结束时间
    product = models.OneToOneField(to=Product)
