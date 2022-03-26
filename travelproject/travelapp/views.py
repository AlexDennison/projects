from django.contrib import messages,auth
from django.shortcuts import redirect, render
from .models import Agency, Place
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    all_places = Place.objects.all()
    all_agencies = Agency.objects.all()
    return render(request,'index.html',{'places':all_places, 'agencies': all_agencies})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('register')
            elif User.objects.filter(email= email).exists():
                messages.info(request,"Email Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,first_name = first_name, last_name=last_name,email =email, password = password)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.info(request,'Password not Matched')
            print("Password not matching")
            return redirect('register')   

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')