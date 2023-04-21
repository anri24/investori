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



 

def komfedencialoba(request):
    return render(request,'komfedencialoba.html')

@login_required(login_url='custom_login')
def profile(request):
    products = request.user.is_resumeuser.order_set.all()
    return render(request, 'main/profile.html')

def video_chat(request):
    return render(request, 'main/videochat.html')

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    # fields = '__all__'
    template_name = 'main/add_comments.html'
    def form_valid(self, form):
        form.instance.product_id=self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('index')

def customers(request):
    if request.user.is_authenticated ==  True:
        datas = Customer.objects.all()
       
        return render(request,'admin_templates/customers.html',{'datas':datas})

    username = request.POST.get('username')
    password = request.POST.get('password')



    user = authenticate(request= request, username=username, password=password)

    if user is not None and user.is_active:
        login(request=request,user = user)
        datas = Customer.objects.all()
       
        return render(request,'admin_templates/customers.html', {'datas':datas})
    else:
        messages.error(request,"Invalid username or password")
        return HttpResponseRedirect(reverse("admin_login"))






def index(request):

    

    Categories = Category.objects.all()
    if 'search' in request.GET:
        search = request.GET['search']
        multiple_q = Q(Q(id__icontains=search) | Q(satauri__icontains=search) | Q(brendi__icontains=search) | Q(modeli__icontains=search))
        products = Product.objects.filter(multiple_q)
    else:
        products=''

    

    

       
    context = {
        'Categories':Categories,
        'products':products,
      
        
        }
    return render(request, 'main/index.html',context)


def product_category(request,cats):
    Categories = Category.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        multiple_q = Q(Q(id__icontains=search) | Q(satauri__icontains=search) | Q(brendi__icontains=search) | Q(modeli__icontains=search))
        products = Product.objects.filter(multiple_q)
    else:
        products=Product.objects.filter(sub_category=cats).order_by('price')or Product.objects.filter(category=cats).order_by('price')
        p=Paginator(products,20)
        page=request.GET.get('page')
        try:
            pages = p.page(page)
        except PageNotAnInteger:
            pages = p.page(1)
        except EmptyPage:
            pages = p.page(p.num_pages)
    context = {
        'cats':cats,
        'Categories':Categories,
        'products':products,
        # 'pages':pages,
        }
    return render(request, 'main/product_category.html',context)


def contact(request):
    return render(request, 'main/contact-us.html')




class CustomProductCreate(LoginRequiredMixin,CreateView):
    model = Product
    fields = ['category','sub_category','garigebis_tipi','name','lokacia','quchis_saxeli','price','telefonis_nomeri','description','photo','photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9','photo10']
    template_name = 'main/add_product.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomProductCreate, self).form_valid(form)


class ProductUpdate(LoginRequiredMixin,UpdateView):
    model = Product
    fields = ['category','sub_category','garigebis_tipi','qonebisTipiHouse','sartuli','sartulebi_sul','sadzineblebi','farti','qonebisTipiCar','brendi','modeli','weli','dzravi','feri','sache','lokacia','quchis_saxeli','satauri','price','telefonis_nomeri','description','photo','photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9','photo10']
    template_name = 'admin_templates/add_product.html'
    success_url = reverse_lazy('admin_login_process')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductUpdate, self).form_valid(form)

class ProductDelete(LoginRequiredMixin,DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'admin_templates/product_delete.html'

    success_url = reverse_lazy('admin_login_process')

class CategoryCreate(LoginRequiredMixin,CreateView):
    model = Category
    fields = ['name']
    template_name = 'admin_templates/add_category.html'
    success_url = reverse_lazy('admin_login_process')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreate, self).form_valid(form)

class CategoryUpdate(LoginRequiredMixin,UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('admin_login_process')




class SubCategoryCreate(LoginRequiredMixin,CreateView):
    model = Sub_Category
    fields = ['name','category']
    template_name = 'admin_templates/add_subcategory.html'
    success_url = reverse_lazy('admin_login_process')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SubCategoryCreate, self).form_valid(form)




@csrf_exempt
def successAddCategory(request):
    
        return HttpResponseRedirect(reverse('admin_login_process'))

   

class ResumeDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'main/single-product.html'


class AdminProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'admin_templates/single_product.html'


def about_us(request):
    return render(request, 'main/about-us.html')



def custom_register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('custom_login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'main/register.html', {'form': form, 'msg': msg})

def custom_login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_resumeuser:
                login(request, user)
                return redirect('index')
           
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'main/login.html', {'form': form, 'msg': msg})





def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_resumeuser:
                login(request, user)
                return redirect('resumes')
           
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})








def registration(request):
    return render(request, 'sendDatas.html')


@csrf_exempt
def addCustomProduct(request):
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

        # if(category != '1') == True:
        #     if(category != '5') == True:
        #         if(len(satauri) < 1):
        #             messages.error(request,"სათაური აუცილებელია")

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
    return render(request,'main/add_product.html',context)

  

@csrf_exempt
def successRegister(request):
    if request.method == 'POST':
    
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dabadebis_dge = request.POST.get('birthday')
        dabadebis_tve = request.POST.get('birthmonth')
        dabadebis_weli = request.POST.get('birthyear')

        country = request.POST.get('country')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        skills = request.POST.get('skills')
        ganatleba = request.POST.get('ganatleba')
        ganatlebis_dawyebis_tve = request.POST.get('start_month')
        ganatlebis_dawyebis_weli = request.POST.get('start_year')
        ganatlebis_damtavrebis_tve = request.POST.get('finish_month')
        ganatlebis_damtavrebis_weli = request.POST.get('finish_year')
        saddaamtavre = request.POST.get('saddaamtavre')


        sv = request.FILES.get('sv')
        number = request.POST.get('number')
        email = request.POST.get('email')

        if(len(firstname) < 1):        
            messages.error(request,"სახელი აუცილებელია")

        if(len(lastname) < 1):        
            messages.error(request,"გვარი აუცილებელია")
            
        if(len(email) < 1 ):        
            messages.error(request,"იმეილი აუცილებელია")


        if Customer.objects.filter(email=email).exists():
            messages.error(request,"იმეილი arsebobs")
            return redirect('registration')

        if(dabadebis_dge == 'none'):        
            messages.error(request,"დაბადების დღე  აუცილებელია")
            return redirect('registration')
        if(dabadebis_tve == 'none'):        
            messages.error(request,"დაბადების თვე  აუცილებელია")
            return redirect('registration')

        if(dabadebis_weli == 'none'):        
            messages.error(request,"დაბადების წელი  აუცილებელია")
            return redirect('registration')



        if(len(country) < 1):        
            messages.error(request,"ქვეყანა აუცილებელია")

        if(len(city) < 1):        
            messages.error(request,"ქალაქი აუცილებელია")



        if(len(skills) < 1):        
            messages.error(request,"სასურველი პოზიცია აუცილებელია")
            return redirect('registration')
            #image
        if(sv == None):        
            messages.error(request,"sv aucilebelia")
            return redirect('registration')

        if(len(number) < 1 ):        
            messages.error(request,"იმეილი აუცილებელია")

        if Customer.objects.filter(phone_number=number).exists():
            messages.error(request,"nomeri arsebobs")
            return redirect('registration')


        if(ganatleba == 'none'):        
            messages.error(request,"განათლება  აუცილებელია")
            return redirect('registration')

        if(ganatlebis_dawyebis_tve == 'none'):        
            messages.error(request,"როდის დაიწყეთ სწავლა(თვე)")
            return redirect('registration')
            
        if(ganatlebis_dawyebis_weli == 'none'):        
            messages.error(request,"როდის დაიწყეთ სწავლა(წელი)")
            return redirect('registration')
            
        if(ganatlebis_damtavrebis_tve == 'none'):        
            messages.error(request,"როდის დაამთავრეთ სწავლა(თვე)")
            return redirect('registration')
            
        if(ganatlebis_damtavrebis_weli == 'none'):        
            messages.error(request,"როდის დაამთავრეთ სწავლა(წელი)")
            return redirect('registration')

        if(len(saddaamtavre) < 1 ):        
            messages.error(request,"სად დაამთავრეთ სწავლა")

       
        form = Customer(phone_number=number,firstname=firstname, lastname=lastname, email=email,country=country,
        city=city,dabadebis_dge=dabadebis_dge,dabadebis_tve=dabadebis_tve,dabadebis_weli=dabadebis_weli,sv=sv,gender=gender,skills=skills,ganatlebis_etapi=ganatleba,start_year=ganatlebis_dawyebis_weli,
        start_month=ganatlebis_dawyebis_tve,end_year=ganatlebis_damtavrebis_weli,end_month=ganatlebis_damtavrebis_tve,sad_miige_ganatleba=saddaamtavre)
        form.save()
        return HttpResponseRedirect(reverse('success'))

    else:
        messages.error(request,"data isn't saved successfully")
        return HttpResponseRedirect(reverse('resumes'))


def success(request):
    return render(request,'success.html')

def check(request):
    return render(request,'check.html')


def adminLogin(request):
    return render(request,"admin_templates/signin.html")



@csrf_exempt
def adminLoginProcess(request):

    if request.user.is_authenticated ==  True:
        Categories = Category.objects.all()
    
        categoryID = request.GET.get('category')
        subcategoryID = request.GET.get('sub_category')

        if categoryID:
            Products = Product.objects.filter(category = categoryID).order_by('price')
            p=Paginator(Products,2)
            page=request.GET.get('page')
            try:
                pages = p.page(page)
            except PageNotAnInteger:
                pages = p.page(1)
            except EmptyPage:
                pages = p.page(p.num_pages)

        elif subcategoryID:
            Products = Product.objects.filter(sub_category = subcategoryID).order_by('price')
            p=Paginator(Products,2)
            page=request.GET.get('page')
            try:
                pages = p.page(page)
            except PageNotAnInteger:
                pages = p.page(1)
            except EmptyPage:
                pages = p.page(p.num_pages)
        else:
            Products = Product.objects.all().order_by('-created_at')
            p=Paginator(Products,2)
            page=request.GET.get('page')
            try:
                pages = p.page(page)
            except PageNotAnInteger:
                pages = p.page(1)
            except EmptyPage:
                pages = p.page(p.num_pages)
        context = {
            'Categories':Categories,
            'Products':Products,
            'pages':pages,
            
            }
       
        return render(request,'admin_templates/home.html',context)

    username = request.POST.get('username')
    password = request.POST.get('password')



    user = authenticate(request= request, username=username, password=password)

    if user is not None and user.is_active:
        login(request=request,user = user)
        datas = Customer.objects.all()
       
        return render(request,'admin_templates/home.html', {'datas':datas})
    else:
        messages.error(request,"Invalid username or password")
        return HttpResponseRedirect(reverse("admin_login"))


def adminLogoutProcess(request):
    logout(request)
    messages.success(request,"logout success")
    return HttpResponseRedirect(reverse("admin_login"))




def customLogoutProcess(request):
    logout(request)
    messages.success(request,"logout success")
    return HttpResponseRedirect(reverse("index"))


class TaskList(LoginRequiredMixin, ListView):
    model = Resume
    context_object_name = 'resumes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumes'] = context['resumes'].filter(user=self.request.user)
        context['count'] = context['resumes'].filter(gamocdileba=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Resume
    context_object_name = 'resume'
    template_name = 'account/resume.html'


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Resume
    fields = ['firstandlastname','photo','number','profesia','email','country','city','skills','shesaxeb','start_month','start_year','end_month','end_year','ganatlebis_etapi','sad_miige_ganatleba','interesebi','gamocdileba']
    
    success_url = reverse_lazy('resumes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    def get_initial(self):
        return { 'photo': ' ' }


class ProductUpdate(LoginRequiredMixin,UpdateView):
    model = Product

    fields = ['category','sub_category','garigebis_tipi','qonebisTipiHouse','sartuli','sartulebi_sul','sadzineblebi','farti','qonebisTipiCar','brendi','modeli','weli','dzravi','feri','sache','satauri','lokacia','quchis_saxeli','price','description','telefonis_nomeri']
    template_name = 'admin_templates/edit_product.html'
    success_url = reverse_lazy('admin_login_process')




class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Resume
    fields = ['firstandlastname','photo','number','profesia','email','country','city','skills','shesaxeb','start_month','start_year','end_month','end_year','ganatlebis_etapi','sad_miige_ganatleba','interesebi','gamocdileba']
    success_url = reverse_lazy('resumes')


class DeleteView(LoginRequiredMixin,DeleteView):
    model = Resume
    context_object_name = 'resume'
    success_url = reverse_lazy('resumes')


