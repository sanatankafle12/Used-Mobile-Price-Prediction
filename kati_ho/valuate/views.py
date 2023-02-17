from django.http import HttpResponse
from . import practice
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Listing

# Create your views here.


def homepage(request):
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(request,'home.html',context)

def listing(request,id):
    listing = Listing.objects.get(id=id)
    context = {
        'listing':listing,
    }
    return render(request,'')

def signuppage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if(pass1!=pass2):
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'register.html')

def loginpage(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, "home.html")

def valuate(request):
    if(request.method == "POST"):
        brandname = request.POST.get('brand')
        print(brandname)
    return render(request,'valuate.html')

def compare(request):
    return render(request,'compare.html')

def recommend(request):
    if(request.method == "POST"):
        brand = request.POST.get("brand_name")
        type1 = request.POST.get('type')
        practice.view(brand,type1)
    return render(request,'recommend.html')

@login_required(login_url='/login/')
def sell_product(request):
    return render(request,'sell_product.html')

def buy(request):
    return render(request,'buy.html')

