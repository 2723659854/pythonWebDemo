# models.py
from django.db import models
# 定义的模型 表名称为Test
class Test(models.Model):
    # 字段name 类型varchar 长度20  （数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度）
    name = models.CharField(max_length=20)
""" 在当前 文件定义表结构 """
class Contact(models.Model):
    # 姓名
    name   = models.CharField(max_length=200)
    # 年龄
    age    = models.IntegerField(default=0)
    # 邮箱
    email  = models.EmailField()
    # 定义一个unicode方法，类似于php的__toString，打印当前对象的name位
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    # 定义一个外键  删除行为: on_delete 是一个参数，用于指定当引用的 Contact 对象被删除时的行为。models.CASCADE 表示级联删除，
    # 即如果 Contact 对象被删除，所有引用它的 Tag 对象也将被自动删除。
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name