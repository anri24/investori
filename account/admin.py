from django.contrib import admin
from .models import User
from .models import *

# Register your models here.

admin.site.register(User)

class Sacheshow(admin.ModelAdmin):
    list_display = ('id','name')

class StatusiShow(admin.ModelAdmin):
    list_display = ('id','saxeli')

class QonebisTipiHouseShow(admin.ModelAdmin):
    list_display = ('id','name')

class QonebisTipiCarShow(admin.ModelAdmin):
    list_display = ('id','name')

class LokaciaShow(admin.ModelAdmin):
    list_display = ('id','name')

class GarigebisTipiShow(admin.ModelAdmin):
    list_display = ('id','saxeli')

class CustomerShow(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','sv','dabadebis_dge','dabadebis_tve','dabadebis_weli','country','city','phone_number','email','gender','created_at')

class ResumeShow(admin.ModelAdmin):
    list_display = ('id','firstandlastname','created')

class CategoryShow(admin.ModelAdmin):
    list_display = ('id','name')

class Sub_CategoryShow(admin.ModelAdmin):
    list_display = ('id','name','category')

class ProductShow(admin.ModelAdmin):
    list_display = ('id','category','sub_category','satauri','price','created_at')

admin.site.register(GarigebisTipi,GarigebisTipiShow)
admin.site.register(Statusi,StatusiShow)
admin.site.register(QonebisTipiHouse,QonebisTipiHouseShow)
admin.site.register(QonebisTipiCar,QonebisTipiCarShow)
admin.site.register(Sache,Sacheshow)

admin.site.register(Lokacia,LokaciaShow)

admin.site.register(Customer,CustomerShow)
admin.site.register(Resume,ResumeShow)
admin.site.register(Category,CategoryShow)
admin.site.register(Sub_Category,Sub_CategoryShow)
admin.site.register(Product,ProductShow)
admin.site.register(Comment)


