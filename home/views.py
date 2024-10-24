from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from home.models import Blog  

# Create your views here.
def index(request):
    gblogs = Blog.objects.all()  
    return render(request, 'index.html', {'gblogs': gblogs, 'user': request.user})

def loginuser(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  
        else:
            messages.error(request, 'Invalid username or password') 

    return render(request, 'login.html')

def blogadd(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    if request.method == "POST":
        topic = request.POST.get("topic")
        text = request.POST.get("text")
        if topic and text: 
            blog = Blog(topic=topic, text=text, author=request.user)  
            blog.save()
            return redirect("/") 
        else:
            messages.error(request, 'Both fields are required.')  

    return render(request, 'addblog.html')

def delete_blog(request, blog_id):

    print(f"Attempting to delete blog with ID: {blog_id}")
    
    blog = get_object_or_404(Blog, id=blog_id) 
    if blog.author == request.user:
        blog.delete()
        messages.success(request, "Blog deleted successfully.")  
        return redirect('home')  
    else:
        messages.error(request, "You are not allowed to delete this blog.") 
        return redirect('home') 

def logoutuser(request):
    logout(request)
    messages.success(request, "Logged out successfully.")  
    return redirect("/login")

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)  
    return render(request, 'blog_detail.html', {'blog': blog})
def info(request):
    return render(request,'info.html')