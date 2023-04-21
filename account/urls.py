from django.urls import path
from django.urls import path
from . import views,adminView
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib import admin



urlpatterns = [

    path('',views.index,name='index'),
    path('konfedencialoba',views.komfedencialoba,name='konfedencialoba'),
    path('product/<int:pk>/comment/', views.AddComment.as_view(), name='add_comment'),

    path('video_chat',views.video_chat,name='video_chat'),
    path('customers',views.customers,name='customers'),


    path('product_category/<str:cats>/',views.product_category,name='product_category'),

    path('about_us',views.about_us,name='about_us'),
    path("product/<int:pk>/", ResumeDetail.as_view(),name="product"),
    path("admin_login_process/product/<int:pk>/", AdminProductDetail.as_view(),name="admin_product"),

    
    path('contact',views.contact,name='contact'),

    path('registration',views.registration,name='registration'),
    path('successRegister',views.successRegister,name='successRegister'),
    path('success',views.success,name='success'),
    path('check',views.check,name='check'),


    path('profile',views.profile,name='profile'),

    path('admin/',views.adminLogin, name="admin_login"),
    path('admin_login_process',views.adminLoginProcess,name='admin_login_process'),
    path('admin_logout_process',views.adminLogoutProcess,name='admin_logout_process'),
    path('create_category',CategoryCreate.as_view(),name='create_category'),
    path('update_category/<int:id>/',CategoryUpdate.as_view(),name='update_category'),

    # path('create_subcategory',views.create_subcategory,name='create_subcategory'),
    path("create_subcategory", SubCategoryCreate.as_view(),name="create_subcategory"),

    # path("add_product", CustomProductCreate.as_view(),name="add_product"),
    path("add_product", views.addCustomProduct,name="add_product"),

    # path("product_create", adminView.ProductCreate.as_view(),name="product_create"),
    path("product_create", adminView.add_Admin_Product,name="product_create"),

    # path('product_update/<int:id>',adminView.Update_Product,name='product_update'),

    path('product_update/<int:pk>',views.ProductUpdate.as_view(),name='product_update'),
    path('product_delete/<int:pk>',views.ProductDelete.as_view(),name='product_delete'),


    path('admin_home', adminView.admin_home,name="admin_home"),

    path('logout/', LogoutView.as_view(next_page = 'login_view'), name='logout'),


    path("resumes", TaskList.as_view(),name="resumes"),
    path("resume/<int:pk>/", TaskDetail.as_view(),name="resume"),
    path("resume-create/", TaskCreate.as_view(),name="resume-create"),
    path("resume-update/<int:pk>/", TaskUpdate.as_view(),name="resume-update"),
    path("resume-delete/<int:pk>/", DeleteView.as_view(),name="resume-delete"),

    path('custom_login/', views.custom_login_view, name='custom_login'),
    path('custom_register/', views.custom_register, name='custom_register'),
    path('custom_logout_process',views.customLogoutProcess,name='custom_logout_process'),

    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

