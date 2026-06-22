from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def sign_up(request):
    if request.method=='POST':
        
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        
        
        if password!=confirm_password:
            messages.error(request,'password do not match!')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'User already exist!')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already existing!')
            return redirect('signup')
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
           
            
        )
        messages.success(request,'Registraion successfully completed')
        
        return redirect('login')
        
        
        
        
    return render(request,'signup.html')


def login_view(request):
    
    if request.method=='POST':
        
        print(request.POST)
        
        
         
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        print(username)
        print(password)
        
        user=authenticate(request,username=username,password=password)
        
        print(user)
        
        if user is not None:
            print("LOGIN SUCCESS")
            login(request,user)
            messages.success(request,'Welcome back')
            return redirect('home')
        
             
           
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('login')
    
    return render(request,'login.html')



@login_required(login_url='login')
def home(request):
    
    
    print(request.user)
    print(request.user.is_authenticated)
    
    
    return render(request,'home.html')


def logout_view(request):

    logout(request)

    return redirect('login')