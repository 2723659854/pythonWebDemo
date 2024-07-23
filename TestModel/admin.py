from django.contrib import admin
from TestModel.models import Test,Contact,Tag
# """ 在当前文件关联表
# python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
# python manage.py migrate TestModel   # 创建表结构

# Register your models here.
# 自定义表单样式
class ContactAdmin(admin.ModelAdmin):
    # 栏位设置
    fieldsets = (
        # 主栏位设置
        ['Main',{
            'fields':('name','email'),
        }],
        # 扩展栏位设置
        ['Advance',{
            # 样式 蜷缩
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
# 将模型和样式关联
admin.site.register(Contact, ContactAdmin)
# 注册模型 实际上就是将模型注册到应用中，在django中，每一个功能模块被封装成了应用
admin.site.register([Test, Tag])