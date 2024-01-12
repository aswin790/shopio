from django.shortcuts import render,redirect
from item.models import category,item
from django.contrib.auth import logout
from . import forms

# Create your views here.

def home(request):
    all_category = category.objects.all()
    filtered_item = item.objects.filter(is_sold = False)
    print(filtered_item)
    return render(request,'core/index.html',{
        'items' : filtered_item,
        'categories' : all_category
    })


def user_signup(request):
    form = forms.signupForm()
    if request.POST:
        print('hello')
        form = forms.signupForm(request.POST)
        print("hi")
        if form.is_valid():
            form.save()
            print("wew")
            return redirect('/login/')
        else:
            print(form.errors)

    return render(request,'user/signup.html',{'form':form})

def user_login(request):
    return render(request,'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')

def contact(request):
    return render(request,'core/contact.html')

