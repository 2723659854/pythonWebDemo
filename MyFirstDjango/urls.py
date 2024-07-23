"""
URL configuration for MyFirstDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

""" 路由配置 """

""" 导入 Django 的管理站点模块，这个模块提供了 Django 自带的管理界面。 """
from django.contrib import admin
""" 导入 path 函数，用于定义 URL 路径和与之对应的视图函数。 """
from django.urls import path
""" 从当前模块（通常是 urls.py 所在的应用）导入 views 模块，以便在 URL 路由中引用视图函数。 """
#from . import views
#from . import testdb
from . import views,testdb,search

""" urlpatterns 是一个包含 URL 路由配置的列表。每个 URL 路由条目都使用 path 函数来定义。 路由表其实就是映射关系 """
urlpatterns = [
    # """ 这个路由将根路径（即 ""，或 /）与 views.hello 视图函数关联起来。 name="hello" 为这个路由命名，可以在其他地方引用它，例如在模板中生成 URL。 """
    path("", views.hello, name="hello"),
    # """ 这个路由将 admin/ 路径与 Django 管理站点的 URL 配置关联起来。 """
    path('admin/', admin.site.urls),
    # 定义一个路由，访问views的runnoob方法
    path('runoob/', views.runoob,name='runoob'),
    # 测试数据库操作
    path('testdb/', testdb.testdb),
    # 查询数据库
    path('query/', testdb.query),
    # 更新
    path('update/', testdb.update),
    # 正则匹配到搜索表单路由
    path('search-form/', search.search_form),
    # 执行搜索
    path('search/', search.search),
    # post方式提交表单
    path('search_post/', search.search_post),
]
