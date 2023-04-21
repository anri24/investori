
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *
from inspect import _empty
from multiprocessing import Value
from queue import Empty
import re
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .admin import Customer
from .models import *
from django.views.decorators.csrf import csrf_exempt

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django. contrib.auth.models import User
from .forms import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required

from django.db.models import Q


@login_required(login_url = "/admin/")
def admin_home(request):
    return render(request, 'admin_templates/home.html')

class ProductCreate(LoginRequiredMixin,CreateView):
    model = Product
    fields = ['category','sub_category','garigebis_tipi','qonebisTipiHouse','sartuli','sartulebi_sul','sadzineblebi','farti','qonebisTipiCar','brendi','modeli','weli','dzravi','feri','sache','lokacia','quchis_saxeli','satauri','price','telefonis_nomeri','description','photo','photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9','photo10']
    template_name = 'admin_templates/add_product.html'
    success_url = reverse_lazy('admin_login_process')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductCreate, self).form_valid(form)


        
@csrf_exempt
@login_required(login_url = "/admin/")
def add_Admin_Product(request):
    categories = Category.objects.all()
    sub_categories = Sub_Category.objects.all()
    garigebisTipi = GarigebisTipi.objects.all()
    qonebisTipiHouse = QonebisTipiHouse.objects.all()
    lokacia = Lokacia.objects.all()
    qonebisTipiCar = QonebisTipiCar.objects.all()
    sache = Sache.objects.all()


    if request.method == 'POST':
        category = request.POST.get('category')
        sub_category = request.POST.get('sub_category')
        garigebis_tipi = request.POST.get('garigebis_tipi')

        # axali manqnis 

        manqnisTipi = request.POST.get('manqnis_tipi')
        brendi = request.POST.get('brendi')
        modeli = request.POST.get('modeli')
        weli = request.POST.get('weli')
        dzravi = request.POST.get('dzravi')
        feri = request.POST.get('feri')
        ruli = request.POST.get('sache')

        # axali saxlis
        saxlisTipi = request.POST.get('saxlis_tipi')
        sartuli = request.POST.get('sartuli')
        sartulebi_sul = request.POST.get('sartulebi_sul')
        sadzineblebi = request.POST.get('sadzineblebi')
        farti = request.POST.get('farti')

        

        # axali sxva
        satauri = request.POST.get('satauri')

        # axali end

        mdebareoba = request.POST.get('adgilmdebareoba')
        quchis_saxeli = request.POST.get('quchis_saxeli')
        price = request.POST.get('price')
        telefonis_nomeri = request.POST.get('telefonis_nomeri')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        photo2 = request.FILES.get('photo2')
        photo3 = request.FILES.get('photo3')
        photo4 = request.FILES.get('photo4')
        photo5 = request.FILES.get('photo5')
        photo6 = request.FILES.get('photo6')
        photo7 = request.FILES.get('photo7')
        photo8 = request.FILES.get('photo8')
        photo9 = request.FILES.get('photo9')
        photo10 = request.FILES.get('photo10')



        if sartuli =='':
            sartuli=None

        if sartulebi_sul =='':
            sartulebi_sul=None

        if sadzineblebi =='':
            sadzineblebi=None

        if farti =='':
            farti=None

        if weli =='':
            weli=None
        if price =='':
            price=None

        if telefonis_nomeri =='':
            telefonis_nomeri=None



        if(category == 'null'):        
            messages.error(request,"კატეგორიის არჩევა აუცილებელია")

        if(sub_category == 'null'):        
            messages.error(request,"ქვეკატეგორიის არჩევა აუცილებელია")

        if(garigebis_tipi == 'null'):        
            messages.error(request,"გარიგების ტიპის არჩევა აუცილებელია")

        if(category == '1') == True:
            if(manqnisTipi == 'null'):
                messages.error(request,"ავტომობილის ტიპი აუცილებელია")

        if(category == '1') == True:
            if(len(brendi) < 1):
                messages.error(request,"ავტომობილის ბრენდი აუცილებელია")

        if(category == '1') == True:
            if(len(modeli) < 1):
                messages.error(request,"ავტომობილის მოდელი აუცილებელია")

        if(category == '1') == True:
            if(weli == None):
                messages.error(request,"ავტომობილის გამოშვების წელი აუცილებელია")

        if(category == '1') == True:
            if(len(dzravi) < 1):
                messages.error(request,"ავტომობილის ძრავი აუცილებელია")

        if(category == '1') == True:
            if(len(feri) < 1):
                messages.error(request,"ავტომობილის ფერი აუცილებელია")

        if(category == '1') == True:
            if(ruli == 'null'):
                messages.error(request,"ავტომობილის საჭე აუცილებელია")

        if(category == '5') == True:
            if(saxlisTipi == 'null'):
                messages.error(request,"უძრავი ქონების ტიპი აუცილებელია")

            
        if(category == '5') == True:
            if(sartuli == None):
                messages.error(request,"უძრავი ქონების სართული აუცილებელია")

        
        if(category == '5') == True:
            if(sartulebi_sul == None):
                messages.error(request,"უძრავი ქონების სართულების რაოდენობა აუცილებელია")


        if(category == '5') == True:
            if(sadzineblebi == None):
                messages.error(request,"უძრავი ქონების საძინებლის რაოდენობა აუცილებელია")

        if(category == '5') == True:
            if(farti == None):
                messages.error(request,"უძრავი ქონების ფართი აუცილებელია")

        # if(category != '1' or category != '5') == True:
        #     if(len(satauri) < 1):
        #         messages.error(request,"სათაური აუცილებელია")

        if(mdebareoba == 'null'):
            messages.error(request,"მდებარეობის არჩევა აუცილებელია")
        
        if(len(quchis_saxeli) < 1):
            messages.error(request,"ქუჩა  აუცილებელია")

        if(price == None):
            messages.error(request,"ფასი  აუცილებელია")

        if(telefonis_nomeri == None):
            messages.error(request,"მობილურის ნომერი აუცილებელია")

        if(photo is None):
            messages.error(request,"მთავარი ფოტო აუცილებელია")

        
        # if(messages.error is Empty):
        form = Product(category_id=category,sub_category_id=sub_category,garigebis_tipi_id=garigebis_tipi,qonebisTipiHouse_id=saxlisTipi,sartuli=sartuli,
        sartulebi_sul=sartulebi_sul,sadzineblebi=sadzineblebi,farti=farti,qonebisTipiCar_id=manqnisTipi,brendi=brendi,modeli=modeli,weli=weli,
        dzravi=dzravi,feri=feri,sache_id=ruli,satauri=satauri,lokacia_id=mdebareoba,
        quchis_saxeli=quchis_saxeli,price=price,telefonis_nomeri=telefonis_nomeri,description=description,photo=photo,photo2=photo2,photo3=photo3,photo4=photo4,photo5=photo5,
        photo6=photo6,photo7=photo7,photo8=photo8,photo9=photo9,photo10=photo10)
        form.save()
        return HttpResponseRedirect(reverse('index'))
    
    context = {
        'categories':categories,
        'sub_categories':sub_categories,
        'garigebisTipi':garigebisTipi,
        'qonebisTipiHouse':qonebisTipiHouse,
        'lokacia':lokacia,
        'qonebisTipiCar':qonebisTipiCar,
        'sache':sache,
    }
    return render(request,'admin_templates/add_product.html',context)


        
@csrf_exempt
@login_required(login_url = "/admin/")
def Update_Product(request,pk):
    categories = Category.objects.all()
    sub_categories = Sub_Category.objects.all()
    garigebisTipi = GarigebisTipi.objects.all()
    qonebisTipiHouse = QonebisTipiHouse.objects.all()
    lokacia = Lokacia.objects.all()
    qonebisTipiCar = QonebisTipiCar.objects.all()
    sache = Sache.objects.all()
    product = Product.objects.all()


    if request.method == 'POST':
        category = request.POST.get('category')
        sub_category = request.POST.get('sub_category')
        garigebis_tipi = request.POST.get('garigebis_tipi')

        # axali manqnis 

        manqnisTipi = request.POST.get('manqnis_tipi')
        brendi = request.POST.get('brendi')
        modeli = request.POST.get('modeli')
        weli = request.POST.get('weli')
        dzravi = request.POST.get('dzravi')
        feri = request.POST.get('feri')
        ruli = request.POST.get('sache')

        # axali saxlis
        saxlisTipi = request.POST.get('saxlis_tipi')
        sartuli = request.POST.get('sartuli')
        sartulebi_sul = request.POST.get('sartulebi_sul')
        sadzineblebi = request.POST.get('sadzineblebi')
        farti = request.POST.get('farti')

        

        # axali sxva
        satauri = request.POST.get('satauri')

        # axali end

        mdebareoba = request.POST.get('adgilmdebareoba')
        quchis_saxeli = request.POST.get('quchis_saxeli')
        price = request.POST.get('price')
        telefonis_nomeri = request.POST.get('telefonis_nomeri')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        photo2 = request.FILES.get('photo2')
        photo3 = request.FILES.get('photo3')
        photo4 = request.FILES.get('photo4')
        photo5 = request.FILES.get('photo5')
        photo6 = request.FILES.get('photo6')
        photo7 = request.FILES.get('photo7')
        photo8 = request.FILES.get('photo8')
        photo9 = request.FILES.get('photo9')
        photo10 = request.FILES.get('photo10')



        if sartuli =='':
            sartuli=None

        if sartulebi_sul =='':
            sartulebi_sul=None

        if sadzineblebi =='':
            sadzineblebi=None

        if farti =='':
            farti=None

        if weli =='':
            weli=None
        if price =='':
            price=None

        if telefonis_nomeri =='':
            telefonis_nomeri=None



        if(category == 'null'):        
            messages.error(request,"კატეგორიის არჩევა აუცილებელია")

        if(sub_category == 'null'):        
            messages.error(request,"ქვეკატეგორიის არჩევა აუცილებელია")

        if(garigebis_tipi == 'null'):        
            messages.error(request,"გარიგების ტიპის არჩევა აუცილებელია")

        if(category == '1') == True:
            if(manqnisTipi == 'null'):
                messages.error(request,"ავტომობილის ტიპი აუცილებელია")

        if(category == '1') == True:
            if(len(brendi) < 1):
                messages.error(request,"ავტომობილის ბრენდი აუცილებელია")

        if(category == '1') == True:
            if(len(modeli) < 1):
                messages.error(request,"ავტომობილის მოდელი აუცილებელია")

        if(category == '1') == True:
            if(weli == None):
                messages.error(request,"ავტომობილის გამოშვების წელი აუცილებელია")

        if(category == '1') == True:
            if(len(dzravi) < 1):
                messages.error(request,"ავტომობილის ძრავი აუცილებელია")

        if(category == '1') == True:
            if(len(feri) < 1):
                messages.error(request,"ავტომობილის ფერი აუცილებელია")

        if(category == '1') == True:
            if(ruli == 'null'):
                messages.error(request,"ავტომობილის საჭე აუცილებელია")

        if(category == '5') == True:
            if(saxlisTipi == 'null'):
                messages.error(request,"უძრავი ქონების ტიპი აუცილებელია")

            
        if(category == '5') == True:
            if(sartuli == None):
                messages.error(request,"უძრავი ქონების სართული აუცილებელია")

        
        if(category == '5') == True:
            if(sartulebi_sul == None):
                messages.error(request,"უძრავი ქონების სართულების რაოდენობა აუცილებელია")


        if(category == '5') == True:
            if(sadzineblebi == None):
                messages.error(request,"უძრავი ქონების საძინებლის რაოდენობა აუცილებელია")

        if(category == '5') == True:
            if(farti == None):
                messages.error(request,"უძრავი ქონების ფართი აუცილებელია")

        # if(category != '1' or category != '5') == True:
        #     if(len(satauri) < 1):
        #         messages.error(request,"სათაური აუცილებელია")

        if(mdebareoba == 'null'):
            messages.error(request,"მდებარეობის არჩევა აუცილებელია")
        
        if(len(quchis_saxeli) < 1):
            messages.error(request,"ქუჩა  აუცილებელია")

        if(price == None):
            messages.error(request,"ფასი  აუცილებელია")

        if(telefonis_nomeri == None):
            messages.error(request,"მობილურის ნომერი აუცილებელია")

        if(photo is None):
            messages.error(request,"მთავარი ფოტო აუცილებელია")


    

        
        # if(messages.error is Empty):
        form = Product(category_id=category,sub_category_id=sub_category,garigebis_tipi_id=garigebis_tipi,qonebisTipiHouse_id=saxlisTipi,sartuli=sartuli,
        sartulebi_sul=sartulebi_sul,sadzineblebi=sadzineblebi,farti=farti,qonebisTipiCar_id=manqnisTipi,brendi=brendi,modeli=modeli,weli=weli,
        dzravi=dzravi,feri=feri,sache_id=ruli,satauri=satauri,lokacia_id=mdebareoba,
        quchis_saxeli=quchis_saxeli,price=price,telefonis_nomeri=telefonis_nomeri,description=description,photo=photo,photo2=photo2,photo3=photo3,photo4=photo4,photo5=photo5,
        photo6=photo6,photo7=photo7,photo8=photo8,photo9=photo9,photo10=photo10)
        form.save()
        return HttpResponseRedirect(reverse('index'))
    
    context = {
        'categories':categories,
        'sub_categories':sub_categories,
        'garigebisTipi':garigebisTipi,
        'qonebisTipiHouse':qonebisTipiHouse,
        'lokacia':lokacia,
        'qonebisTipiCar':qonebisTipiCar,
        'sache':sache,
        'product':product
    }
    return render(request,'admin_templates/edit_product.html',context)