from django.shortcuts import render
from set.models import Set
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
# Create your views here.

@login_required
def set_manage(request):
    username = request.session.get('user','')
    set_list = Set.objects.all()
    paginator = Paginator(set_list, 8)  # 生成paginator对象，设置每页显示8条记录
    page = request.GET.get('page', 1)  # 获取当前页码数，默认为第1页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        set_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        set_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第一页内容
    except EmptyPage:
        set_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页内容
    return  render(request,"set_manage.html",{"user":username,"sets":set_list})

@login_required
def set_user(request):
    user_list = User.objects.all()
    username = request.session.get('user','')
    return render(request,"set_user.html",{'user':username,'users':user_list})

@login_required
def setsearch(request):
    username = request.session.get('user','')
    search_setname = request.GET.get("setname","")
    set_list = Set.objects.filter(setname__icontains=search_setname)
    return render(request,"set_manage.html",{"user":username,"sets":set_list})