from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get("name","").strip()
        email = request.POST.get("email", "").strip().lower()
        phone = request.POST.get("phone", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        profile_photo = request.FILES.get("profile_photo")
        if not name or not email or not phone or not password:
            return render(request,'register.html', {'error': 'Please fill all the field!'})
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Password did not match!'})
        if CustomUser.objects.filter(email=email).exists():
            return render(request,'register.html', {'error':'Email Exists. Use another!'})
        if CustomUser.objects.filter(phone = phone).exists():
            return render(request,'register.html', {'error':'Phone Number Exists. Use another!'})
        
        CustomUser.objects.create_user(
            name = name,
            email=email,
            phone=phone,
            password=password,
            profile_photo = profile_photo
        )
        return redirect("member_login")

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email","").strip().lower()
        password = request.POST.get("password","")

        user = authenticate(
            request,
            email = email,
            password = password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('Home')
        return render(request, "login.html",{"error":"User Not Found!"})


    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, "profile.html")

def auth_logout(request):
    logout(request)
    return redirect('Home')