from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserForm,UserSignUpForm, BlogForm

from .models import UserBlog
from .models import UserBlog
# Create your views here.
def home(request):
    return render(request, 'django_task3_app/home.html')

def login(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'django_task3_app/login.html', {'form': form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/success')



def signup(request):
    if request.method == "GET":
        form = UserSignUpForm()
        return render(request, 'django_task3_app/signup.html', {'form': form})
    else:
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')

def createblog(request, id=0):
    if request.method == "GET":
        if id == 0:  # for create
            form = BlogForm()
        else:
            blog = UserBlog.objects.get(pk=id)
            form = BlogForm(instance=blog)
        return render(request, 'django_task3_app/blog.html', {'form': form})
    else:
        if id==0:
            form = BlogForm(request.POST)
        else:
            blog = UserBlog.objects.get(pk=id)
            form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
        return redirect('/success')

def success(request):
    context = {'blog_list': UserBlog.objects.all()}
    return render(request, 'django_task3_app/success.html', context)


def deleteUser(request, id):
    user = UserBlog.objects.get(pk=id)
    user.delete()
    return redirect('/success')


def logout_request(request):
    logout(request)
    return redirect('/login')
