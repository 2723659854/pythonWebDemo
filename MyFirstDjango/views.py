# 引入http响应
from django.http import HttpResponse
# 模板渲染
from django.shortcuts import render

import datetime
# 定义函数hello
def hello(request):
    # 当接收到请求的时候，返回响应字符串
    return HttpResponse("Hello world ! ")
# 定义一个runoob方法
def runoob(request):
    # 创建一个字典，类似于php的对象
    context          = {}
    # 设置变量
    context['hello'] = 'Hello World!'
    # 调用模型渲染
    # return HttpResponse("runoob.html")
    views_list = ["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
    # 我擦呢，这python的语法是依靠空格分割语句的，多一个空格都无法运行，
    views_dict = {"name":"菜鸟教程"}
    # 获取当前时间
    now  = datetime.datetime.now()
    # 数据
    views_num = 88
    # 列表2
    views_list2 = ["菜鸟教程","菜鸟教程1","菜鸟教程2","菜鸟教程3",]

    data = [
        {"name": "tom", "age": 17, "sex": "girl"},
        {"name": "jerry", "age": 18, "sex": "boy"},
        {"name": "anna", "age": 16, "sex": "girl"},
    ]

    # 打印结果
    # print(data)



    return render(request, 'runoob.html', {
        "views_list": views_list,
        "views_dict": views_dict,
        "now":now,"num":views_num,
        "list":views_list2,
        "data":data
        })