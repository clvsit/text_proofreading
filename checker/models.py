from django.db import models
from mongoengine import Document, StringField, IntField


class FeedBack(Document):
    id = StringField(max_length=36)
    document = StringField()
    start = IntField(max_length=8)
    end = IntField(max_length=8)
    answer = StringField(max_length=24)
    confidence = StringField(max_length=10)
    type = IntField(max_length=1)
    date = StringField(max_length=19)
    remark1 = StringField()
    remark2 = StringField()


class AdminRole(models.Model):
    id = models.AutoField("角色ID", primary_key=True)
    name = models.CharField('角色名称', max_length=12)
    authority = models.CharField("角色权限", max_length=24)
    brief = models.CharField("简要介绍", max_length=64)
    create_date = models.DateField("创建日期", auto_now=True)
    modify_date = models.DateField("修改日期", auto_now=True)
    reason = models.CharField("修改原因", max_length=64)
    remark1 = models.CharField("备注1", max_length=64, blank=True)
    remark2 = models.CharField("备注2", max_length=64, blank=True)

    def __str__(self):
        return self.name


class AdminUser(models.Model):
    account = models.CharField('用户账号', primary_key=True, max_length=32)
    password = models.CharField('用户密码', max_length=32)
    name = models.CharField('用户姓名', max_length=4)
    role_id = models.ForeignKey(AdminRole, on_delete=models.CASCADE, default=2)
    create_date = models.DateField("创建日期", auto_now=True)
    modify_date = models.DateField("修改日期", auto_now=True)
    reason = models.CharField("修改原因", max_length=64)
    remark1 = models.CharField("备注1", max_length=64, blank=True)
    remark2 = models.CharField("备注2", max_length=64, blank=True)

    def __str__(self):
        return self.name
