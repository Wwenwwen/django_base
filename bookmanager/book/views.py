from django.shortcuts import render

# Create your views here.
"""
    所谓的视图其实就是Python函数
    两个要求：
        1 视图函数的第一个参数用于接受请求
        2 必须返回一个响应
"""
from django.http import HttpRequest
from django.http import HttpResponse

# 我们希望用户输入http://127.0.0.1:8000/index/进行访问视图函数
def index(request):
    # return HttpResponse('ok')
    # request
    # template_name
    # context = None
    context = {
        'name':"点我有惊喜"
    }
    return render(request,template_name='book/index.html',context=context)