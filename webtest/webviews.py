from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webtest.models import Webcasestep,Webcase
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

# Create your views here.

@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get('user','')
    paginator = Paginator(webcase_list, 8)  # 生成paginator对象，设置每页显示8条记录
    page = request.GET.get('page', 1)  # 获取当前页码数，默认为第1页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        webcase_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        webcase_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第一页内容
    except EmptyPage:
        webcase_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页内容
    return render(request,"webcase_manage.html",{"user":username,"webcases":webcase_list})

@login_required
def webcasestep_manage(request):
    username = request.session.get('user','')
    webcasestep_list = Webcasestep.objects.all()
    paginator = Paginator(webcasestep_list, 8)  # 生成paginator对象，设置每页显示8条记录
    page = request.GET.get('page', 1)  # 获取当前页码数，默认为第1页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        webcasestep_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        webcasestep_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第一页内容
    except EmptyPage:
        webcasestep_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页内容
    return render(request, "webcasestep_manage.html",{"user":username,"webcasesteps":webcasestep_list})

@login_required
def websearch(request):
    username = request.session.get('user','')
    search_webcasename = request.GET.get("webcasenaem","")
    webcase_list = Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request,'webcase_manage.html',{'user':username,'webcases':webcase_list})

@login_required
def webstepsearch(request):
    username = request.session.get('user','')
    search_webcasename = request.GET.get("webcasename","")
    webcasestep_list = Webcasestep.objects.filter(webcasennamne__icontains=search_webcasename)
    return render(request,'webcasestep_manage.html',{'user':username,'webcasesteps':webcasestep_list})
