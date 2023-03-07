from django.http import HttpResponse
from . import valuateprice,recommendmobile,comparemobile
from django.shortcuts import render,redirect,get_object_or_404
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
        price_dict = {'price1':"The Predicted Price is: " + str(round(price1[0],2))}
        ram = request.POST.get('ram')
        return render(request,"valuate.html",price_dict)
    return render(request,'valuate.html')

def compare(request):
    my_object = get_object_or_404(Listing,id=5)
    my_object2 = get_object_or_404(Listing,id=6)
    phone_1 = {'Brand':my_object.brand,'Model':my_object.model,'Price':my_object.price,'Condition':my_object.condition,'Battery':my_object.battery,'Storage':my_object.storage,'Ram':my_object.ram,'Front Camera':my_object.front_camera,'Back Camera': my_object.back_camera,'Size':my_object.size,'Resolution':my_object.res}
    phone_2 = {'Brand':my_object2.brand,'Model':my_object2.model,'Price':my_object2.price,'Condition':my_object2.condition,'Battery':my_object2.battery,'Storage':my_object2.storage,'Ram':my_object2.ram,'Front Camera':my_object2.front_camera,'Back Camera': my_object2.back_camera,'Size':my_object2.size,'Resolution':my_object2.res}
    compared_list = comparemobile.compare(phone_1,phone_2)
    compared_list = {'Brand':compared_list[0],'Model':compared_list[1],'Price':compared_list[2],'Condition':compared_list[3],'Battery':compared_list[4],'Storage':compared_list[5],'Ram':compared_list[6],'Front_Camera':compared_list[7],'Back_Camera': compared_list[8],'Size':compared_list[9],'Resolution':compared_list[10],'gaming':compared_list[11],'general':compared_list[12],'photography':compared_list[13],'movie':compared_list[14]}
    return render(request, 'compare.html',{'phone':my_object,'phone2':my_object2,'compared':compared_list})

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
        data = {
                "String": "RECOMMENDED MODEL: ",
                "Price": "Price = " + str(data1['Price'].values[0]),
                "Model":"Model = "+ str(data1['Model'].values[0]),
                "Brand":"Brand = "+ str(data1['brand'].values[0])}
        return render(request,'recommend.html',data)
    return render(request,'recommend.html')

@login_required(login_url='/login/')
def sell_product(request):
    form = valuate_listing()
    if request.method == 'POST':
        form = valuate_listing(data=request.POST,files=request.FILES)
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


