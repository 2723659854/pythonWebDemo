"""
ASGI config for MyFirstDjango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
""" asgi.py 文件为 Django 项目提供了与 ASGI 兼容的入口点，使得项目可以利用异步编程的优势，从而支持现代 Web 应用的各种需求。
如果你的应用需要处理实时通信、长连接或高并发请求，使用 ASGI 和配置 asgi.py 文件是非常重要的步骤。 """

""" os 模块用于与操作系统交互。 """
import os

""" 创建 ASGI 应用程序 """
from django.core.asgi import get_asgi_application

""" 这行代码设置环境变量 DJANGO_SETTINGS_MODULE，指定 Django 项目的设置文件位置 """
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirstDjango.settings')
""" 这行代码调用 get_asgi_application 函数，返回一个 ASGI 应用程序对象。ASGI 服务器会使用这个对象来处理请求。 """
application = get_asgi_application()
