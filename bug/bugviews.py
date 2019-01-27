from django.shortcuts import render
from bug.models import Bug
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def bug_manage(request):
    username = request.session.get('user','')
    bug_list = Bug.objects.all()
    paginator = Paginator(bug_list, 8)  # 生成paginator对象，设置每页显示8条记录
    page = request.GET.get('page', 1)  # 获取当前页码数，默认为第1页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        bug_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        bug_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第一页内容
    except EmptyPage:
        bug_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页内容
    return render(request,"bug_manage.html",{"user":username,"bugs":bug_list})