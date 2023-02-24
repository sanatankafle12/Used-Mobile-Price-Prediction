from django.http import HttpResponse
from . import practice,valuateprice,recommendmobile
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import valuate_listing


def homepage(request):
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(request,'home.html',context)


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
    return homepage(request)

def valuate(request):
    if(request.method == "POST"):
        brandname = request.POST.get('brand')
        Initial_price = request.POST.get('initial')
        battery_condition = request.POST.get('battery')
        display_condition = request.POST.get('display')
        audio_condition = request.POST.get('Speaker')
        phone_condition = request.POST.get('Scratches')
        age = request.POST.get('age')
        warranty = request.POST.get('warranty')
        earphone = request.POST.get('Earphone')
        charger = request.POST.get('charger')
        price1 = valuateprice.valuate1([[int(Initial_price),int(age),int(battery_condition),int(display_condition),int(audio_condition),int(phone_condition),int(warranty),int(earphone),int(charger)]])
        price_dict = {'price1':price1}
        ram = request.POST.get('ram')
        print(brandname,ram)
        return render(request,"valuate.html",price_dict)
    return render(request,'valuate.html')

def compare(request):
    return render(request,'compare.html')

def recommend(request):
    if(request.method == "POST"):
        ram = request.POST.get('ram')
        want = request.POST.get('want')
        battery = request.POST.get('battery')
        price = request.POST.get('price')
        Storage = request.POST.get('Storage')
        back_camera = request.POST.get('back_camera')
        front_camera = request.POST.get('front_camera')
        screen_size = request.POST.get('screen_size')
        res = request.POST.get('resolution')
        width,height = res.split('x')
        pixels = int(width)*int(height)
        os =request.POST.get('os')
        data1 = recommendmobile.rec_func([[int(price),int(front_camera),int(back_camera),int(battery),int(os),int(Storage),int(ram),8,pixels]])
        data = {"Price":data1['Price'].values[0],
                "Model":data1['Model'].values[0],
                "Ram":data1['ram'].values[0]}
        return render(request,'recommend.html',data)
    return render(request,'recommend.html')

@login_required(login_url='/login/')
def sell_product(request):
    form = valuate_listing()
    if request.method == 'POST':
        form = valuate_listing(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        print(form)
        form = valuate_listing()
    context = {
        'form':form
    }
    return render(request,'sell_product.html',context)


