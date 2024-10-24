from django.contrib import admin
from django.urls import path, include
from home import views
from .views import index, blog_detail 
urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.loginuser, name="login"),
    path('addblog/', views.blogadd, name="addblog"),
    path('logout/', views.logoutuser, name="logout"), 
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),  
    path('info/', views.info , name="info"),
]
