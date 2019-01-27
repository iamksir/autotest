from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
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

@login_required
def apistepsearch(request):
    username = request.session.get('user','')
    searche_apiname = request.GET.get("apiname",'')
    apistep_list = Apistep.objects.filter(apiname__icontains=searche_apiname)
    return render(request,'apistep_manage.html',{'user':username,'apisteps':apistep_list})

@login_required
def apissearch(request):
    username = request.session.get('user', '')
    search_apiname = request.GET.get("apiname", '')
    apis_list = Apis.objects.filter(apiname__icontains=search_apiname)
    return render(request, 'apis_manage.html', {"user": username, "apiss": apis_list})

'''接口管理'''
#流程接口管理
@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all() #读取所有流程接口数据
    username = request.session.get('user','')
    paginator = Paginator(apitest_list,8) #生成paginator对象，设置每页显示8条记录
    page = request.GET.get('page',1) #获取当前页码数，默认为第1页
    currentPage=int(page) #把获取的当前页码数转换成整数类型
    try:
        apitest_list = paginator.page(page) #获取当前页码数的记录列表
    except PageNotAnInteger:
        apitest_list = paginator.page(1) #如果输入的页数不是整数，则显示第一页内容
    except EmptyPage:
        apitest_list = paginator.page(paginator.num_pages) #如果输入的页数不在系统的页数中，则显示最后一页内容
    return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list}) #定义流程接口数据的变量并返回到前端

'''接口步骤管理'''
@login_required
def apistep_manage(request):
    username = request.session.get('user','')
    apistep_list = Apistep.objects.all()
    paginator = Paginator(apistep_list, 8)  # 生成paginator对象，设置每页显示8条记录
    page = request.GET.get('page', 1)  # 获取当前页码数，默认为第1页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        apistep_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        apistep_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第一页内容
    except EmptyPage:
        apistep_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页内容
    return render(request,'apistep_manage.html',{"user":username,"apisteps":apistep_list})

'''单一接口管理'''
@login_required
def apis_manage(requuest):
    username = requuest.session.get('user','')
    apis_list = Apis.objects.all()
    paginator = Paginator(apis_list, 8)  # 生成paginator对象，设置每页显示8条记录
    page = requuest.GET.get('page', 1)  # 获取当前页码数，默认为第1页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        apis_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        apis_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第一页内容
    except EmptyPage:
        apis_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页内容
    return render(requuest,"apis_manage.html",{"user":username,"apiss":apis_list})

def logout(request):
    auth.logout(request)
    return render(request,"login.html")