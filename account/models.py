from timeit import default_timer
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
import datetime
from django.contrib.auth.models import User

from random import randint
import time
import random







class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_admin= models.BooleanField('Is admin', default=False)
    is_resumeuser = models.BooleanField('Is resumeUser', default=True)
    firstname = models.CharField(max_length=255,null=True)
    lastname = models.CharField(max_length=255,null=True)
    piradinomeri = models.IntegerField(null=True)
    telefonis_nomeri = models.IntegerField(null=True)
    dabadebis_dge = models.IntegerField(null=True)
    dabadebis_tve = models.IntegerField(null=True)
    dabadebis_weli = models.IntegerField(null=True)
    qveyana = models.CharField(max_length=255,null=True)
    qalaqi = models.CharField(max_length=255,null=True)




class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class GarigebisTipi(models.Model):
    id = models.AutoField(primary_key=True)
    saxeli = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.saxeli


class Statusi(models.Model):
    id = models.AutoField(primary_key=True)
    saxeli = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.saxeli


# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)



    

# four = random_with_N_digits(4)

# named_tuple = time.localtime() # get struct_time
# time_string = time.strftime("%Y%m%d%H%M%S", named_tuple)

# randSum = time_string + str(four)


class QonebisTipiHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class QonebisTipiCar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lokacia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Sache(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=True,blank=True)
    garigebis_tipi= models.ForeignKey(GarigebisTipi,on_delete=models.CASCADE,null=True,blank=True)


    qonebisTipiHouse = models.ForeignKey(QonebisTipiHouse,on_delete=models.CASCADE,null=True,blank=True)
    sartuli =  models.IntegerField(null=True,blank=True)
    sartulebi_sul =  models.IntegerField(null=True,blank=True)
    sadzineblebi =  models.IntegerField(null=True,blank=True)
    farti =  models.IntegerField(null=True,blank=True)

    
    qonebisTipiCar= models.ForeignKey(QonebisTipiCar,on_delete=models.CASCADE,null=True,blank=True)
    brendi =  models.CharField(max_length=255,null=True,blank=True)
    modeli =  models.CharField(max_length=255,null=True,blank=True)
    weli =  models.IntegerField(null=True,blank=True)
    dzravi =  models.CharField(max_length=255,null=True,blank=True)
    feri =  models.CharField(max_length=255,null=True,blank=True)
    sache = models.ForeignKey(Sache,on_delete=models.CASCADE,null=True,blank=True)


    satauri =  models.CharField(max_length=255,null=True,blank=True)


    lokacia = models.ForeignKey(Lokacia,on_delete=models.CASCADE,null=True,blank=True)
    quchis_saxeli =  models.CharField(max_length=255,null=True,blank=True)
    price= models.IntegerField(null=True,blank=True)
    description = models.TextField(max_length=1000,null=True,blank=True)
    telefonis_nomeri = models.IntegerField(null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    photo = models.FileField(null=True, blank=True, upload_to="products/")
    photo2 = models.FileField(null=True, blank=True, upload_to="products/")
    photo3 = models.FileField(null=True, blank=True, upload_to="products/")
    photo4 = models.FileField(null=True, blank=True, upload_to="products/")
    photo5 = models.FileField(null=True, blank=True, upload_to="products/")
    photo6 = models.FileField(null=True, blank=True, upload_to="products/")
    photo7 = models.FileField(null=True, blank=True, upload_to="products/")
    photo8 = models.FileField(null=True, blank=True, upload_to="products/")
    photo9 = models.FileField(null=True, blank=True, upload_to="products/")
    photo10 = models.FileField(null=True, blank=True, upload_to="products/")

    dasturi = models.IntegerField(null=True, blank=True)


    
    def __str__(self):
        return self.satauri

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,related_name='comments', on_delete=models.CASCADE) 
    full_name = models.CharField(max_length=255,null=True)
    comment = models.TextField(null=True)
    created_at= models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.full_name)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.IntegerField(null=True,unique=True)

    firstname = models.CharField(max_length=255,null=True)
    lastname = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True,default="")
    dabadebis_dge = models.IntegerField(null=True)
    dabadebis_tve = models.IntegerField(null=True)
    dabadebis_weli = models.IntegerField(null=True)

    country = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=255,null=True)


    skills = models.CharField(max_length=555,null=True)
# news

    YEAR_CHOICES = [(y,y) for y in range(1968, datetime.date.today().year+1)]
    MONTH_CHOICE = [(m,m) for m in range(1,13)]

    start_year = models.IntegerField(choices=YEAR_CHOICES,null=True)
    start_month = models.IntegerField(choices=MONTH_CHOICE,null=True)
    end_year = models.IntegerField(choices=YEAR_CHOICES,null=True)
    end_month = models.IntegerField(choices=MONTH_CHOICE,null=True)

    ganatlebis_etapi = models.CharField(max_length=255,null=True)

    sad_miige_ganatleba = models.CharField(max_length=255,null=True)



# end news
    sv = models.ImageField(null=True, blank=True, upload_to="resumes/")
    
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname




   


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    id = models.AutoField(primary_key=True)

    firstandlastname = models.CharField(max_length=255,null=True)
    photo = models.ImageField(null=True, blank=True, upload_to="photos/")

    number = models.IntegerField(null=True)
    profesia = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True,default="")
    country = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)

    skills = models.CharField(max_length=555,null=True)
# news
    shesaxeb = models.CharField(max_length=1000,null=True)

    YEAR_CHOICES = [(y,y) for y in range(1968, datetime.date.today().year+1)]
    MONTH_CHOICE = [(m,m) for m in range(1,13)]

    start_year = models.IntegerField(choices=YEAR_CHOICES,null=True)
    start_month = models.IntegerField(choices=MONTH_CHOICE,null=True)
    end_year = models.IntegerField(choices=YEAR_CHOICES,null=True)
    end_month = models.IntegerField(choices=MONTH_CHOICE,null=True)

    ganatlebis_etapi = models.CharField(max_length=255,null=True)

    sad_miige_ganatleba = models.CharField(max_length=255,null=True)

    interesebi = models.CharField(max_length=1000,null=True)

    gamocdileba = models.CharField(max_length=1000,null=True)
    created = models.DateTimeField(auto_now_add=True)

# end news
    

    def __str__(self):
        return self.firstandlastname

