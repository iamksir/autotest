from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
#产品管理
@login_required
def product_manage(request):
    username = request.session.get('user','')
    product_list = Product.objects.all()
    return render(request,"product_manage.html",{"user":username,"products":product_list})