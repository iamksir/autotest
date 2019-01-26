﻿from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apitest.models import Apistep,Apitest,Apis


def home(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username",'')
        password = request.POST.get("password",'')
        if username == '' or password == '':
            return render(request,'login.html',{'error':"用户名或密码为空"})
        else:
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request,user)
                response = HttpResponseRedirect("/home/")
                request.session["user"] = username
                return response
            else:
                return render(request,"login.html",{"error":"用户名或密码错误！"})
    else:
        return render(request,"login.html")

@login_required
def left(request):
    return render(request,"left.html")

@login_required
def apisearch(request):
    username = request.session.get('user','')
    search_apitestname = request.GET.get("apitestname",'')
    apitest_list = Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request,'apitest_manage.html',{"user":username,"apitests":apitest_list})

'''接口管理'''
@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all() #读取所有流程接口数据
    username = request.session.get('user','')
    return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list}) #定义流程接口数据的变量并返回到前端

'''接口步骤管理'''
@login_required
def apistep_manage(request):
    username = request.session.get('user','')
    apistep_list = Apistep.objects.all()
    return render(request,'apistep_manage.html',{"user":username,"apisteps":apistep_list})

'''单一接口管理'''
@login_required
def apis_manage(requuest):
    username = requuest.session.get('user','')
    apis_list = Apis.objects.all()
    return render(requuest,"apis_manage.html",{"user":username,"apiss":apis_list})

def logout(request):
    auth.logout(request)
    return render(request,"login.html")