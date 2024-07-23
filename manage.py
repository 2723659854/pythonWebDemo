#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# 命令行工具
# os 模块用于与操作系统进行交互，主要用于设置环境变量。
import os
# sys 模块提供对 Python 解释器的访问，包括命令行参数。
import sys

# 定义入口函数
def main():
    # 配置项目参数
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirstDjango.settings')
    try:
        # 引入命令行处理工具
        from django.core.management import execute_from_command_line
        # 如果引入失败
    except ImportError as exc:
        # 抛出异常 你确定你已经安装了，确认已经将python加入到环境变量了，是否忘记激活虚拟环境
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 获取用户参数，并执行
    execute_from_command_line(sys.argv)

""" 如果是直接执行，而不是作为模块引入，则执行main()函数 """
if __name__ == '__main__':
    main()
