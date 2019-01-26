from django.contrib import admin
from product.models import Product

# Register your models here.
class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename','webtestresult','creat_time','id','product']

class ProductAdmin(admin.ModelAdmin):
    list_display = ["productname",'productdesc','producter',"creat_time","id"]
    inlines = [WebcaseAdmin]

admin.site.register(Product) #讲产品模块注册到Django admin后台并显示