from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
#产品管理
@login_required
def product_manage(request):
    username = request.session.get('user','')
    product_list = Product.objects.all()
    paginator = Paginator(product_list,8)
    page = request.GET.get('page',1)
    currentPage = int(page)
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)
    return render(request,"product_manage.html",{"user":username,"products":product_list})

@login_required
def productsearch(request):
    username = request.session.get('user','')
    search_productname = request.GET.get("productname","")
    product_list = Product.objects.filter(productname__icontains=search_productname)
    return render(request,'product_manage.html',{"user":username,"products":product_list})