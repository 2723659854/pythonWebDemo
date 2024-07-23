from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf

# 表单
def search_form(request):
    # 直接渲染模板
    return render(request, 'search_form.html')

# 接收请求数据
def search(request):
    # 强制设置编码格式为UTF8
    request.encoding='utf-8'
    # 检查请求的 GET 参数中是否包含键 'q'，并且该键的值是否非空。request.GET 是一个 QueryDict 对象，包含所有 GET 请求的参数。
    if 'q' in request.GET and request.GET['q']:
        # 拼接内容
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
    # 初始化内容
    ctx ={}
    # 如果是post提交方式
    if request.POST:
        # 获取参数并赋值
        ctx['rlt'] = request.POST['q']
    # 渲染
    return render(request, "post.html", ctx)
